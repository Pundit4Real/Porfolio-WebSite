from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100, default="")

class AboutMe(models.Model):
    intro_img = models.ImageField(upload_to='about/')
    intro_text_title = models.CharField(max_length=110)
    intro_text = models.TextField(max_length=400,null=True, blank=True)
    #skills 
    skills_img = models.ImageField(upload_to='about/')
    skills_text_title = models.CharField(max_length=110)
    skills_text = models.TextField(max_length=500,null=True, blank=True)

class Projects(models.Model):
    ...

