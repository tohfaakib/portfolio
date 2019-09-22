# Generated by Django 2.2.5 on 2019-09-22 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_set', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('professional_title', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='pro_img')),
                ('skills', models.ManyToManyField(to='biography.Skills')),
            ],
        ),
    ]
