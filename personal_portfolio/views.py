from django.shortcuts import render

from projects.models import Project, Project_Category
from cv.models import CV
from biography.models import Biography
from social.models import Social

from utils.logics import lengthMeasure  # additional logics

def base(request):
    projects = Project.objects.all()
    categories = Project_Category.objects.all()
    biography = Biography.objects.all()
    cv = CV.objects.all().order_by('-created_at')
    socials = Social.objects.all()

    biography = lengthMeasure(biography)
    skills = biography.skills.all()

    cv = lengthMeasure(cv)



    context = {
        'projects': projects,
        'categories': categories,
        'cv': cv,
        'biography': biography,
        'skills': skills,
        'socials': socials
    }

    return render(request, 'base.html', context)
