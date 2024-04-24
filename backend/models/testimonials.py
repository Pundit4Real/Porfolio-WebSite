from django.db import models


class TestimonialHero(models.Model):
    title = models.CharField(max_length=120,default='')
    desc = models.TextField(default='')

    class Meta:
        verbose_name_plural = 'Testimonial Hero'

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=55,default='')
    quote = models.TextField(default='')
    image = models.ImageField(upload_to='testimonial')
    com_image = models.ImageField(upload_to='testimonial_com_image',default='')
    role = models.CharField(max_length=130,default='')

    class Meta:
        verbose_name_plural = 'Testimonial'

    def __str__(self):
        return self.name