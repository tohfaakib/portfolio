# Generated by Django 2.2.5 on 2019-09-26 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]