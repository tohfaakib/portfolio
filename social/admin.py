from django.contrib import admin
from .models import Social


class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_url')


admin.site.register(Social, SocialAdmin)


