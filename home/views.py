<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):   
    return render(request,'index.html/');
def adopt(request):
    return render(request,'adopt.html/');
def docs(request):
    return render(request,"docs.html/");
def helpline(request):
    return render(request,"helpline.html/");


from .models import BlogPost
from .forms import BlogPostForm

def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  
    else:
        form = BlogPostForm()
    return render(request, 'add_blog_post.html', {'form': form})

def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})

from django.shortcuts import render, get_object_or_404
from .models import Pet

def adopt_list(request):
    pets = Pet.objects.filter(is_adopted=False)
    return render(request, 'adopt_list.html', {'pets': pets})

def adopt_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'adopt_detail.html', {'pet': pet})



# views.py in hello app

=======
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
>>>>>>> 88c2577a0f202bf1f43ee1d32770d3c1962c9df4
