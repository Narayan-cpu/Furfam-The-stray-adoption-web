<<<<<<< HEAD
from django.db import models
from django.conf import settings


class Contact(models.Model):
    name = models.CharField(max_length=112)
    email = models.CharField(max_length=112)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
       return self.name
   
    


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title
  

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pets/', null=True, blank=True)
    is_adopted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    


# for login


# models.py in hello app
# hello/models.py

# hello/models.py


# hello/models.py

=======
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=112)
    email = models.CharField(max_length=112)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
       return self.name
    


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title
>>>>>>> 88c2577a0f202bf1f43ee1d32770d3c1962c9df4
