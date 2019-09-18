from django.shortcuts import render

from projects.models import Project, Project_Category

def base(request):
    projects = Project.objects.all()
    categories = Project_Category.objects.all()
    context = {
        'projects': projects,
        'categories': categories
    }
    return render(request, 'base.html', context)
