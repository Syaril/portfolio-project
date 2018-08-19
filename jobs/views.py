from django.shortcuts import render

from .models import Job

def home(request):
    user = request.user
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs, 'user':user})

