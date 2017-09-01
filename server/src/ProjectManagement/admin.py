from django.contrib import admin

from .models import Project,Task

class ProjectAdmin(admin.ModelAdmin):
	list_display = ["id", "title","description", "status", "prioirity", "men_hours", "income" , "start_date" ,"end_date","timestamp", "updated", "active"]

admin.site.register(Project, ProjectAdmin)


class TaskAdmin(admin.ModelAdmin):
	list_display = ["id", "title","description", "status", "prioirity", "men_hours", "start_date" ,"end_date","timestamp", "updated", "active"]

admin.site.register(Task, TaskAdmin)