from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tag, Blog
from .forms import CreateBlogForm, UpdateBlogForm



# List Published Blogs
def Home(request):
    blog = Blog.objects.filter(is_published=True)
    tag = Tag.objects.all()
    context = {
        'tags': tag,
        'blogs': blog,
    }
    return render(request, 'blog/index.html', context)


# Create Blog
@login_required
def Createblog(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateBlogForm()
    return render(request, 'blog/create-blog.html',{'form':form})

# Update Blog
@login_required
def Updateblog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = UpdateBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = UpdateBlogForm(instance=blog)
    return render(request,'blog/update-blog.html',{'form':form})

# Blog Detail
def Blogdetail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    tags = blog.tags.all()
    context = {
        'blog': blog,
        'tags': tags,
    }
    return render(request, 'blog/blog-detail.html', context)