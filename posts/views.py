from django.shortcuts import render
from .models import Post

# Create your views
def post_list(request):
    data = Post.objects.all()
    return render(request,'posts/index.html',{'posts':data})

def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'posts/detail.html',{'posts':data})