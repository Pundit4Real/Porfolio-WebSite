from django.db import models


class ServiceHero(models.Model):
    title = models.CharField(max_length=100,default='')
    description = models.TextField(max_length=300,default='')
    class Meta:
        verbose_name_plural = 'ServiceHero'

    def __str__(self):
        return self.title
    

class Services(models.Model):
    service_no = models.IntegerField(default='0')
    service_title = models.CharField(max_length=150,default='')
    service_desc = models.TextField(max_length=300,default='')

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service_title
    

class ServicePopUp(models.Model):
    service_title = models.ForeignKey(Services, on_delete=models.CASCADE)
    modal_img = models.ImageField(upload_to='popUp modal',default='')
    sub_title = models.CharField(max_length=100,default='')
    title = models.CharField(max_length=100,default='')
    description = models.TextField(max_length=700,default='')
