from django.db import models


class ServiceHero(models.Model):
    title = models.CharField(max_length=100,default='')
    description = models.TextField(max_length=300,default='')
    class Meta:
        verbose_name_plural = 'Service Hero'

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
    description = models.TextField(max_length=700,default='')
    process_descr = models.TextField(max_length=400,default='')
    Process_list = models.CharField(max_length=1000, blank=True)

    def get_list(self):
        return self.Process_list.split(',') if self.Process_list else []

    def set_list(self, value):
        self.Process_list = ','.join(value)

    list_property = property(get_list, set_list)

    class Meta:
        verbose_name_plural = 'Service Pop-Up'
        

