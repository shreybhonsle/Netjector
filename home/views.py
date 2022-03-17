from django.shortcuts import render,HttpResponse,redirect
from home.models import *
from django.contrib import messages
from blog.models import Featured,Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

#HTML RENDERING
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']

        if len(name) <2 or len(email)<9 or len(phone)< 13 or len(content)<4:
            messages.error(request,'Form not submitted. Kindly fill information correctly.')
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'Thanks for submitting form. We will reach you out shortly.')
    return render(request, "home/contact.html")

def search(request):
    query = request.GET['query']   
    post = Post.objects.filter(title__icontains=query)
    featured =  Featured.objects.filter(title__icontains=query)      
    params = {'allpost':post,'featured':featured}
    return render(request,'home/search.html',params)

#Authentication
def handlesignup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.firstname = firstname
        myuser.lastname = lastname
        myuser.save()
        if len(username)>13:
            messages.error(request,"Username : Length of username should be less than 13 characters. ")
            return redirect('/') 
        if pass1 != pass2:
            messages.error(request,"Password : Password DoNot Match. ")
            return redirect('/')
        else:
            messages.success(request,"Your account has been successfully created !!!")
            return redirect('/')
    else:
        return HttpResponse("404 - NOT ALLOWED")

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(request,username=loginusername,password=loginpass)
        if user != None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request,"Invalid User/Password. SignUp if not registerd. ")
            return redirect('/')
    else:
        return HttpResponse('404 - NOT FOUND')

def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')