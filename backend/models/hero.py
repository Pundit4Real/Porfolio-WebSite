from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hero(models.Model):
    title1 = models.CharField(max_length=200,default='')
    title2 = models.CharField(max_length=200,default='')
    sub_title = models.CharField(max_length=100,default='')
    logo      = models.ImageField(upload_to='logo',default='')
    favicon = models.ImageField(upload_to='favicon',default='')
    hero_image = models.ImageField(upload_to='hero')
    cv          = models.FileField(upload_to='cv',default='Cv.pdf')                 
    description = models.TextField(max_length=500,default='')
    years_exp = models.IntegerField(default=1)
    no_completed_proj = models.IntegerField(default=1)
    no_clients = models.DecimalField(max_digits=1000000,decimal_places=2,default=1)

    class Meta:
        verbose_name_plural = 'Hero'

    def __str__(self):
        return self.title1

class ProjectPorfolio(models.Model):
    header = models.CharField(max_length=200)
    Description = models.TextField(null=True,blank=True)

class Projects(models.Model):
    cartegory = models.CharField(max_length=200)
    type = models.CharField(max_length=200,null=True)
    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.cartegory


class Works(models.Model):
    cartegory = models.ForeignKey(Projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='works/',null=True,blank=True )
    link = models.URLField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=False,null=True, blank=True)


    class Meta:
        verbose_name_plural = "Works"


    def __str__(self):
        return self.title

    



