from django.shortcuts import render,redirect
from .models import *
from .forms import *



# List Published Blogs
def Home(request):
    return render(request, 'blog/index.html')

# Create Blog
def Createblog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateBlog()
    return render(request, 'blog/create-blog.html',{'form':form})

# Update Blog
def Updateblog(request, slug):
    blog = Blog.objects.filter(slug=slug)
    if request.method == 'POST':
        form = request.POST(request.post, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = request.post(instance=blog)
    return render(request,'blog/update-blog.html',{'form':form})