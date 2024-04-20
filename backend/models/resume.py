from django.db import models


class ResumeHero(models.Model):
    exp_title = models.CharField(max_length=150,default='')
    edu_title = models.CharField(max_length=150,default='')

    class Meta:
        verbose_name_plural = 'ResumeHero'

    def __str__(self):
        return self.exp_title + self.edu_title
    

class Experience(models.Model):
    duration = models.CharField(max_length=100,default='')
    role = models.CharField(max_length=100,default='Software Engineer')
    company = models.CharField(max_length=200,default='')

    class Meta:
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.role



class Education(models.Model):
    duration = models.CharField(max_length=50,default='')
    course_title = models.CharField(max_length=200,default='')
    institute = models.CharField(max_length=250,default='')
    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.institute
