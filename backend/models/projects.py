from django.db import models

class PortfolioHero(models.Model):
    title = models.CharField(max_length=150,default='')
    description = models.TextField(max_length=350,default='')

    class Meta:
        verbose_name_plural = 'Portfolio Hero'

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100,default='')

    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name
    
class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    class Meta:
        verbose_name_plural = 'Portfolio Items'

    def __str__(self):
        return self.title

class PortfolioPopup(models.Model):
    modal_img = models.ImageField(upload_to='Porfolio-popUp-modal -image',default='')
    title = models.CharField(max_length=100)
    description = models.TextField()
    live_preview_link = models.URLField()
    category = models.CharField(max_length=50)
    start_date = models.DateField()
    client = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    project_desc = models.TextField(default='')
    story = models.TextField(default='')
    approach = models.TextField(default='')
    portfolio_item = models.OneToOneField(PortfolioItem, on_delete=models.CASCADE, related_name='popup',default='')
    previous_project = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='next_project_rel', null=True, blank=True)
    next_project = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='previous_project_rel', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Portfolio Popups'

    def __str__(self):
        return self.title


class PortfolioPopupImage(models.Model):
    popup = models.ManyToManyField(PortfolioPopup, related_name='images')
    image = models.ImageField(upload_to='popup_images/')