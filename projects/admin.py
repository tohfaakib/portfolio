from django.contrib import admin
from .models import Project, Project_Category


class ProjectAdmin(admin.ModelAdmin):
    fields = ('categories', 'title', 'description', 'technology', 'image', 'url')
    list_display = ('title', 'technology', 'url')


admin.site.register(Project, ProjectAdmin)

admin.site.register(Project_Category)

