from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post)   # post in admin seite anmelden
