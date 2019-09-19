from django.db import models

# Create your models here.

class CV(models.Model):
    file = models.FileField(upload_to="files")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return "CV"