from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm

# Create your views
def post_list(request):
    data = Post.objects.all()
    return render(request,'posts/index.html',{'posts':data})

def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'posts/detail.html',{'posts':data})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = PostForm()
    
    return render(request,'posts/new.html',{'form':form})

def edit_post(request,post_id):
    data = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = PostForm(instance=data)
    
    return render(request,'posts/edit.html',{'form':form})


def delet_post(request,post_id):
    data = Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog/')