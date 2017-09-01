from django.contrib import admin
from accounts.models import *

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "join_at", "birthday", "timestamp", "updated", "active"]
admin.site.register(Subscriber, SubscriberAdmin)

class TeamAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "timestamp", "updated", "active"]
admin.site.register(Team, TeamAdmin)

class CompanyAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "timestamp", "updated", "active"]

admin.site.register(Company, CompanyAdmin)

class TeamTreeAdmin(admin.ModelAdmin):
	list_display = ["id", "parent", "child", "timestamp", "updated", "active"]

admin.site.register(TeamTree, TeamTreeAdmin)

class CompanySubscriberAdmin(admin.ModelAdmin):
	list_display = ["id", "company", "subscriber", "timestamp", "updated", "active"]

admin.site.register(CompanySubscriber, CompanySubscriberAdmin)

class CompanyTeamAdmin(admin.ModelAdmin):
	list_display = ["id", "company", "team", "timestamp", "updated", "active"]

admin.site.register(CompanyTeam, CompanyTeamAdmin)

class TeamSubscriberAdmin(admin.ModelAdmin):
	list_display = ["id", "team", "subscriber","manager", "job_title", "timestamp", "updated", "active"]

admin.site.register(TeamSubscriber, TeamSubscriberAdmin)