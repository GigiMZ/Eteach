from django import forms
from django.utils.html import format_html

from .models import User


class UserForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'new_password', 'first_name', 'last_name', 'age',
                'profile_pic', 'is_active', 'is_staff',
                'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined']

    def save(self, commit=True):
        res = super().save(commit)
        if self.cleaned_data.get('new_password'):
            self.instance.set_password(self.cleaned_data.get('new_password'))
        return res
