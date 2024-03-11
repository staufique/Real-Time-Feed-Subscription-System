from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'channel_subscription')
    search_fields = ('username', 'email')
    list_filter = ('channel_subscription',)
    ordering = ('id',)
    filter_horizontal = ()
admin.site.register(User, CustomUserAdmin)
