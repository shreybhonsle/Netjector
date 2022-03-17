from django.shortcuts import render,HttpResponse,redirect
from blog.models import *
from django.contrib import messages
from blog.templatetags import extras
from django.views.generic import CreateView
import random
import string
import re


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

# Create your views here.
def blogHome(request):
    allpost = Post.objects.all()
    allfeatured = Featured.objects.all()
    topPost = Featured.objects.all()
    final = Featured.objects
    for post in allfeatured:
            
        final = post
        cont = post.content
        post.content= cleanhtml(cont)
    for post in allpost:
        cont = post.content
        post.content= cleanhtml(cont)
    

    context = {'allpost':allpost,'featured':allfeatured,'topPost':topPost}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug= slug).first()
    comments = blogcomment.objects.filter(post=post,parent=None)
    replies = blogcomment.objects.filter(post=post).exclude(parent=None)
    context = {'post':post,'comments':comments}
    repDict={}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno]= [reply]
        else:
            repDict[reply.parent.sno].append(reply)
    isfeatured = 1
    if post == None:
        post = Featured.objects.filter(slug= slug).first()
        context = {'post':post,'comments':None}
        isfeatured = None 
    context = {'post':post,'comments':comments,'isfeatured':isfeatured,'user':request.user,'replyDict': repDict}
    return render(request,'blog/blogPost.html',context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        parentSno = request.POST.get("parentSno")
        post = Post.objects.get(sno=postSno)  
        parent="" 
        slug = post.slug
        if parentSno=="":          
            comment = blogcomment(comment=comment,user=user,post=post)
            comment.save()        
            messages.success(request,"Your comment has been posted sucessfully")
        else:
            parent = blogcomment.objects.get(sno=parentSno)
            comment = blogcomment(comment=comment,user=user,post=post,parent=parent)
            comment.save()        
            messages.success(request,"Your reply has been posted sucessfully")        
        return redirect("/blog/"+slug)

def writeBlog(request):
    return render(request,'blog/writeblog.html')


def postblog(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.user 
    slug =  ''.join((random.choice(string.ascii_lowercase) for x in range(50)))
    p = Post(title=title,content=content,author=author,slug=slug)
    p.save()
    print(title)
    print(content)
    print(author)
    print(slug)
    return redirect('/blog')