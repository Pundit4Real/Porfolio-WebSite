from django.db import models

class PortfolioHero(models.Model):
    title = models.CharField(max_length=150,default='')
    description = models.TextField(max_length=350,default='')

    class Meta:
        verbose_name_plural = 'PortfolioHero'

    def __str__(self):
        return self.title
    

class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('uxui', 'UX/UI'),
        ('branding', 'Branding'),
        ('mobile-app', 'Mobile App'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    modal_content = models.OneToOneField('PortfolioPopup', on_delete=models.CASCADE, related_name='portfolio_item')

    class Meta:
        verbose_name_plural = 'PortfolioItems'

    def __str__(self):
        return self.title


class PortfolioPopup(models.Model):
    title = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    category = models.CharField(max_length=50,default='')
    client = models.CharField(max_length=100 ,default='')
    start_date = models.DateField()
    designer = models.CharField(max_length=100 ,default='')
    project_description = models.TextField(default='')
    story = models.TextField(default='')
    approach = models.TextField(default='')

    # Assuming a one-to-many relationship between PortfolioPopup and images in the gallery
    # You may need to adjust this depending on your actual implementation
    gallery_images = models.ManyToManyField('GalleryImage', related_name='popup')

    class Meta:
        verbose_name_plural = 'PortfolioPopups'
        
    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='portfolio_gallery_images/')
    portfolio_item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name='gallery_images',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'GalleryImages'
        
    def __str__(self):
        return self.image.name
