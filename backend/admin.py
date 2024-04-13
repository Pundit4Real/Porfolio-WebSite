from django.contrib import admin
from backend.models import (Profile, AboutMe,Projects,Works,
                            ProjectPorfolio)
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'image']
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['header', 'intro_img','intro_text_title','skills_img','skills_text_title']
class WorksAdmin(admin.ModelAdmin):
    list_display = ['id','title','cartegory', 'image','link']

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['cartegory', 'type']


admin.site.register(Profile,ProfileAdmin)
admin.site.register(AboutMe,AboutMeAdmin)
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(Works,WorksAdmin)
admin.site.register(ProjectPorfolio)


