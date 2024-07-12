from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('adopt.html/',views.adopt,name='adopt'),
    path('docs.html/',views.docs,name='docs'),
    path('helpline.html/',views.helpline,name='helpline'),
        path('blog/add/', views.add_blog_post, name='add_blog_post'),
    path('blog/', views.blog_list, name='blog_list'),
]

# main_app/urls.py
#from django.urls import path
#from . import views

#urlpatterns = [

    # Add other URLs as needed
#]
