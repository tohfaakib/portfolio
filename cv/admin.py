from django.contrib import admin
from .models import CV, IP


class CVAdmin(admin.ModelAdmin):
    # fields = ('created_at', 'updated_at')
    list_display = ('created_at', 'updated_at', 'total_download', 'unique_download')


admin.site.register(CV, CVAdmin)
admin.site.register(IP)
