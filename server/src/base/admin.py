from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
	list_display = ["title","description", "slug", "imageSrc", "button_text", "timestamp", "updated", "active"]

admin.site.register(Product, ProductAdmin)

# ========================================

# class GroupAdmin(admin.StackedInline):
# 	list_display = ["name"]
# 	filter_horizontal = ('members')

# admin.site.register(Group, GroupAdmin)