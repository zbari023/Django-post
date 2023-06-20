from django.contrib import admin

# Register your models here, admin panal form
from .models import Post, Author

class PostAdmin(admin.ModelAdmin):
    list_display =['title' , 'date']
    list_filter = ['date' , 'author','tags']

admin.site.register(Post,PostAdmin)   # post in admin seite anmelden
admin.site.register(Author) 
