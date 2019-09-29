from django.db import models

# Create your models here.

class Social(models.Model):
    name = models.CharField(max_length=100)
    profile_url = models.URLField()
    favicon = models.ImageField(upload_to='icon')

    def __str__(self):
        return self.name

