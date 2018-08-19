from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Blog

@login_required
def allblogs(request):
    user=request.user
    getblogs = Blog.objects.filter(user__username=user)
    return render(request, 'blog/allblogs.html', {'getblogs': getblogs, 'username':user})

@login_required
def detail(request, blog_id):
    detailed_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detailed.html', {'blog': detailed_blog})

@login_required
def create(request):
    if request.method == "POST":
        try:
            request.POST['is_important'] == 'on'
            blog = Blog()
            blog.title = request.POST['title']
            blog.pub_date = timezone.datetime.now()
            blog.body = request.POST['body']
            blog.image = request.FILES['image']
            blog.is_important = True
            blog.user = request.user
            blog.save()
            return redirect('allblogs')
        except:
            return render(request, 'blog/create.html',
                          {'error': 'please confirm that you understand that this information is confidential'})
    return render(request, 'blog/create.html')