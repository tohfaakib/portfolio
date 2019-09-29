from django.db import models

# Create your models here.


class IP(models.Model):
    ip_list = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.ip_list


class CV(models.Model):
    file = models.FileField(upload_to="files")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    total_download = models.IntegerField(default=0, null=True, blank=True)
    unique_download = models.IntegerField(default=0, null=True, blank=True)
    ip = models.ManyToManyField(IP, blank=True)


    def __str__(self):
        return "CV"
