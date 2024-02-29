from django.shortcuts import render,redirect
from .models import *
from .forms import *



# List Published Blogs
def Home(request):
    tags = Tag.objects.all()
    return render(request, 'blog/index.html', {'tags':tags})

# Create Blog
def Createblog(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateBlogForm()
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