from django.contrib import admin
from backend.models import Profile, AboutMe,Projects,Works
# Register your models here.

admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(AboutMe)
admin.site.register(Works)

