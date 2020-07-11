from django.shortcuts import render
from .models import ProjectApplication, ProjectAppsUse, ProjectCourse, ProjectHabit


# Create your views here.

def projects(request):
    applications = ProjectApplication.objects.all().order_by('id')
    apps = ProjectAppsUse.objects.all().order_by('id')
    courses = ProjectCourse.objects.all().order_by('id')
    habits = ProjectHabit.objects.all().order_by('id')

    context = {
        'applications': applications,
        'apps': apps,
        'courses': courses,
        'habits': habits,
    }
    return render(request, 'projects.html', context)
