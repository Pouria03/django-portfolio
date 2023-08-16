from django.shortcuts import render
from home_app import models

# Create your views here.
def index_view(request):
    home_data = models.Home.objects.last()
    about_data = models.About.objects.last()
    skills = models.Skill.objects.all()
    services = models.Service.objects.all()
    resumes = models.Resume.objects.all()

    context = {
        'home_data': home_data,
        'about_data': about_data,
        'skills': skills,
        'services': services,
        'resumes': resumes,
    }

    return render(request, 'home_app/index.html',context)