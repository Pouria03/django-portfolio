from django.shortcuts import render
from home_app import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


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


@csrf_exempt
def send_message_view(request):
    if request.method == 'POST':
        try:
            msg = models.UserMessage()
            msg.name = request.POST.get('name', 'none')
            msg.phone = request.POST.get('phone', 'none')
            msg.email = request.POST.get('email', 'none')
            msg.body = request.POST.get('content', 'none')
            msg.save()
            return JsonResponse({'success': True, 'message': 'Message sent successfully'})
        except Exception:
            return JsonResponse({'success': False, 'message': 'Invalid request method'})


