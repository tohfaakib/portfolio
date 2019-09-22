from django.db import models

# Create your models here.

class Skills(models.Model):
    skill_set = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_set


class Biography(models.Model):
    name = models.CharField(max_length=200)
    professional_title = models.CharField(max_length=200)
    about = models.TextField()
    skills = models.ManyToManyField(Skills)
    image = models.ImageField(upload_to="pro_img")

    def __str__(self):
        return self.name
