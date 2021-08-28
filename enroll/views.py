from django.shortcuts import render, redirect
from .models import *
from .forms import postForm
# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'enroll/home.html', context)


def addPost(request):
    

    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
      form = postForm()
    
    context = {'form': form}
    return render(request, 'enroll/addPost.html',context)