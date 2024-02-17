from django.shortcuts import render
from .models import *
from .forms import *



# List Published Blogs
def Home(request):
    return render(request, 'blog/index.html')

# Create Blog
def Createblog(request):
    form = CreateBlog()
    return render(request, 'blog/create-blog.html',{'form':form})