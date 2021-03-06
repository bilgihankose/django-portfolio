from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblog.html', {'blogs': blogs})

def blogdetail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogdetail.html', {'blogdetail': blogdetail})