from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    getblogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'getblogs': getblogs})

def detail(request, blog_id):
    detailed_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detailed.html', {'blog': detailed_blog})