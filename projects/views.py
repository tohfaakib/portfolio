from django.shortcuts import render
from .models import Project

from cv.models import CV
from biography.models import Biography

# Create your views here.

def project_index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,

    }
    return render(request, 'project/index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    cv = CV.objects.all().order_by('-created_at')
    biography = Biography.objects.all()[0]
    skills = biography.skills.all()

    if len(cv) > 0:
        cv = cv[0]
    else:
        cv = ''

    context = {
        'project': project,
        'cv': cv,
        'biography': biography,
        'skills': skills
    }
    return render(request, 'project/detail.html', context)