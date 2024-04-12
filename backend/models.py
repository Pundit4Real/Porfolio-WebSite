from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100, default="")

    class meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    header = models.CharField(max_length=100)
    intro_img = models.ImageField(upload_to='about/')
    intro_text_title = models.CharField(max_length=110)
    intro_text = models.TextField(max_length=400,null=True, blank=True)
    #skills 
    skills_img = models.ImageField(upload_to='about/')
    skills_text_title = models.CharField(max_length=110)
    skills_text = models.TextField(max_length=500,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'About Me'

    def __str__(self):
        return self.header

class Projects(models.Model):
    cartegory = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.cartegory


class Works(models.Model):
    cartegory = models.ForeignKey(Projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True,blank=True)
    image = models.ImageField(upload_to='works/')
    link = models.URLField(max_length=200)


    class Meta:
        verbose_name_plural = "Works"


    def __str__(self):
        return self.title

    


