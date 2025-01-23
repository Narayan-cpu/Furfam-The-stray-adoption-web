from django.contrib import admin

# Register your models here.

from .models import BlogPost

admin.site.register(BlogPost)


from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'is_adopted')
    list_filter = ('breed', 'is_adopted')
    search_fields = ('name', 'breed')





#added

# home/admin.py

