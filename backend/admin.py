from django.contrib import admin
from backend.models.hero import (Hero,Projects,Works,
                            ProjectPorfolio)
# Register your models here.

class HeroAdmin(admin.ModelAdmin):
    list_display = ['sub_title', 'title1','title2','hero_image','description']
class WorksAdmin(admin.ModelAdmin):
    list_display = ['id','title','cartegory', 'image','link']

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['cartegory', 'type']


admin.site.register(Hero,HeroAdmin)
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(Works,WorksAdmin)
admin.site.register(ProjectPorfolio)


