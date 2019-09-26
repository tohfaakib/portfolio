from django.db import models

# Create your models here.

class Project_Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    categories = models.ForeignKey('Project_Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img")
    video = models.URLField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title