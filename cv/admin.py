from django.contrib import admin
from .models import CV


class CVAdmin(admin.ModelAdmin):
    # fields = ('created_at', 'updated_at')
    list_display = ('created_at', 'updated_at', 'download_count')


admin.site.register(CV, CVAdmin)
