from django.contrib import admin
from django.urls import path
from home import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='home'),
    path('adopt.html/',views.adopt,name='adopt'),
    path('docs.html/',views.docs,name='docs'),
    path('helpline.html/',views.helpline,name='helpline'),
        path('blog/add/', views.add_blog_post, name='add_blog_post'),
    path('blog/', views.blog_list, name='blog_list'),
        path('adopt/', views.adopt_list, name='adopt_list'),
    path('adopt/<int:pet_id>/', views.adopt_detail, name='adopt_detail'),

]


# main_app/urls.py
#from django.urls import path
#from . import views

#urlpatterns = [

    # Add other URLs as needed
#]
