from django.db import models

class SkillsHero(models.Model):
    title = models.CharField(max_length=200,default='')
    description = models.TextField(max_length=350,default='')

    class Meta:
        verbose_name_plural = 'SkillsHero'

    def __str__(self):
        return self.title
    

class Skills(models.Model):
    skills_img = models.ImageField(upload_to='skills-img',default='img.jpg')
    rating_percentage = models.IntegerField(default=50)
    skills_title = models.CharField(max_length=70,default='python')
    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skills_title
    