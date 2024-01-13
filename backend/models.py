from django.db import models

# Create your models here.

class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField()
    