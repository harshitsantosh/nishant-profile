from django.contrib import admin
from .models import ProjectApplication, ProjectAppsUse, ProjectCourse, ProjectHabit

# Register your models here.

admin.site.register(ProjectApplication)
admin.site.register(ProjectAppsUse)
admin.site.register(ProjectCourse)
admin.site.register(ProjectHabit)
