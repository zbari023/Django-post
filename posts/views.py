from django.shortcuts import render
from .models import Post

# Create your views
def post_list(request):
    data = Post.objects.all()
    return render(request,'posts/index.html',{'posts':data})