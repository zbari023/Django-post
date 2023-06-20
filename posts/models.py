from django.db import models

# Create your models here, post erstellen, bd designing, bei eine zugefügte in models muss folgendes gemacht werden: python manage.py makemigrations ; python manage.py migrate
class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    Content = models.TextField(max_length=15000)
    
    
    
