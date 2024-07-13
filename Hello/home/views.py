from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):   
    return render(request,'index.html/');
def adopt(request):
    return render(request,'adopt.html/');
def docs(request):
    return render(request,"docs.html/");
def helpline(request):
    return render(request,"helpline.html/");

from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # Replace with your actual URL name for blog list
    else:
        form = BlogPostForm()
    return render(request, 'add_blog_post.html', {'form': form})

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})
