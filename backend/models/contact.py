from django.db import models

class ContactUsHero(models.Model):
    title = models.CharField(max_length=200,default='')
    desc = models.CharField(max_length=300,default='')

    class Meta:
        verbose_name_plural = 'Contact Us Hero'

    def __str__(self):
        return self.title
class ContactUs(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    service = models.CharField(max_length=200)
    message = models.TextField(max_length=200)

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


    def __str__(self):
        return self.first_name