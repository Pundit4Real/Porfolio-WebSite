from django.contrib import admin
from backend.models.hero import Hero
from backend.models.services import ServiceHero,Services,ServicePopUp
from backend.models.contact import ContactUs,ContactUsHero
# Register your models here.

class HeroAdmin(admin.ModelAdmin):
    list_display = ['sub_title', 'title1','title2','hero_image','description']

class ServiceHeroAdmin(admin.ModelAdmin):
    list_display = ['title','description']

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['service_no','service_title','service_desc']

class ServicePopUpAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'modal_img',]

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','email','phone','service','message']

class ContactUsHeroAdmin(admin.ModelAdmin):
    list_display = ['title','phone','email','address']



admin.site.register(Hero,HeroAdmin)
admin.site.register(ServiceHero,ServiceHeroAdmin)
admin.site.register(Services,ServicesAdmin)
admin.site.register(ServicePopUp,ServicePopUpAdmin)
admin.site.register(ContactUs,ContactUsAdmin)
admin.site.register(ContactUsHero,ContactUsHeroAdmin)



