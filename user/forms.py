from django import forms
from .models import User


class UserForm(forms.ModelForm):
    new_password = forms.PasswordInput()

    class Meta:
        model = User
        fields = "__all__"