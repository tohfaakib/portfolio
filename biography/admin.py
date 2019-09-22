from django.contrib import admin
from .models import Biography, Skills


class BiographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'professional_title', 'about', 'image')


admin.site.register(Biography, BiographyAdmin)

admin.site.register(Skills)

