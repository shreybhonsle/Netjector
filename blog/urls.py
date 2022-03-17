from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('postComment',views.postComment,name="postComment"),
    path('writeBlog',views.writeBlog,name="writeBlog"),
    path('postblog',views.postblog,name="postblog"),
    path('<str:slug>', views.blogPost, name='blogPost'),
    
]

