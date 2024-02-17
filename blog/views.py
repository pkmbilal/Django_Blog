from django.shortcuts import render
from .models import *


# List Published Blogs
def home(request):
    return render(request, 'blog/index.html')

# Create Blog
def CreateBlog(request):
    pass