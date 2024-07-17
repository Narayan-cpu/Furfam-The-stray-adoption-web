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
