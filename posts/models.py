from django.db import models
from taggit.managers import TaggableManager      # -----------

# Create your models here, post erstellen, bd designing, bei eine zugefügte in models muss folgendes gemacht werden: python manage.py makemigrations ; python manage.py migrate
# ; python manage.py runserver

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    image = models.ImageField(upload_to='Author')
    def __str__(self):                                # um in adminpanel den name zu ändern
        return self.name




class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    Content = models.TextField(max_length=15000)
    author = models.ForeignKey(Author,related_name='post_Author',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Post')
    tags = TaggableManager()
    def __str__(self):
        return self.title
    
    
    
