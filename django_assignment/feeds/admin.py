from django.contrib import admin
# from .models import DistributedData
# # Register your models here.
# @admin.register(DistributedData)
# class DistributedAdmin(admin.ModelAdmin):
#     list_display=['channel_group']

from .models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','channel_subscription']