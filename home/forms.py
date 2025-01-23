<<<<<<< HEAD
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author_name']


# forms.py

from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'age', 'description', 'image']




#login pages
# home/forms.py

# home/forms.py


=======
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author_name']
>>>>>>> 88c2577a0f202bf1f43ee1d32770d3c1962c9df4
