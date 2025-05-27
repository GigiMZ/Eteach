from django.contrib import admin
from .models import User
from django.utils.html import format_html
from .forms import UserForm


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'age', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username']
    list_filter = ['is_active', 'is_staff', 'is_superuser']

    readonly_fields = ['profile_image_display']
    # fields = ['username', 'email', 'first_name', 'last_name', 'age',
    #           'profile_image_display', 'profile_pic', 'is_active', 'is_staff',
    #           'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined']

    form = UserForm

    fieldsets = (
        ("User's info", {
            'fields': ('username', 'email', ('first_name', 'last_name'), 'new_password', 'age', 'profile_image_display', 'profile_pic')
        }),
        ('Status', {
            'fields': (('is_active', 'is_staff', 'is_superuser'))
        }),
        ('Groups&Permissions', {
            'fields': ('groups', 'user_permissions')
        }),
        ('Date', {
            'fields': ('date_joined', 'last_login')
        })
    )

    def profile_image_display(self, obj):
        if obj.profile_pic: return format_html(f'<img src="{obj.profile_pic.url}" width="200px"/>')

