from django.shortcuts import render

from projects.models import Project, Project_Category
from cv.models import CV

def base(request):
    projects = Project.objects.all()
    categories = Project_Category.objects.all()
    cv = CV.objects.all().order_by('-created_at')[0]

    context = {
        'projects': projects,
        'categories': categories,
        'cv': cv
    }
    return render(request, 'base.html', context)
