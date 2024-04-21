from django.contrib import admin
from backend.models.hero import Hero
from backend.models.services import ServiceHero,Services,ServicePopUp
from backend.models.contact import ContactUs,ContactUsHero
from backend.models.resume import ResumeHero,Education,Experience
from backend.models.skills import Skills,SkillsHero
# Register your models here.

class HeroAdmin(admin.ModelAdmin):
    list_display = ['sub_title', 'title1','title2','hero_image','description']

class ServiceHeroAdmin(admin.ModelAdmin):
    list_display = ['title','description']

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['service_title','service_no','service_desc']

class ServicePopUpAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'modal_img',]

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','email','phone','service','message']

class ContactUsHeroAdmin(admin.ModelAdmin):
    list_display = ['title','phone','email','address']
class ResumeHeroAdmin(admin.ModelAdmin):
    list_display = ['exp_title','edu_title']

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company','role','duration']
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institute','course_title','duration']

class SkillsHeroAdmin(admin.ModelAdmin):
    list_display = ['title','description','id']
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['skills_img','rating_percentage','skills_img']



admin.site.register(Hero,HeroAdmin)
admin.site.register(ServiceHero,ServiceHeroAdmin)
admin.site.register(Services,ServicesAdmin)
admin.site.register(ServicePopUp,ServicePopUpAdmin)
admin.site.register(ContactUs,ContactUsAdmin)
admin.site.register(ContactUsHero,ContactUsHeroAdmin)
admin.site.register(ResumeHero,ResumeHeroAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(SkillsHero,SkillsHeroAdmin)
admin.site.register(Skills,SkillsAdmin)



