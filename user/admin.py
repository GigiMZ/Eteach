from django.contrib import admin
from .models import User
from django.utils.html import format_html


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'age', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    readonly_fields = ['profile_image_display', 'password']
    fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
              'profile_image_display', 'profile_pic', 'is_active', 'is_staff',
              'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined']

    def profile_image_display(self, obj):
        if obj.profile_pic: return format_html(f'<img src="{obj.profile_pic.url}" width=400/>')