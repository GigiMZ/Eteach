from django import forms
from .models import User
from post.models import Post, Comment
from django.contrib.admin import widgets


class UserAdminForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    up_voted_posts = forms.ModelMultipleChoiceField(
        widget=widgets.FilteredSelectMultiple('Up Voted Posts', False),
        queryset=Post.objects.all(),
        required=False
    )
    up_voted_comments = forms.ModelMultipleChoiceField(
        widget=widgets.FilteredSelectMultiple('Up Voted Comments', False),
        queryset=Comment.objects.all(),
        required=False
    )
    down_voted_posts = forms.ModelMultipleChoiceField(
        widget=widgets.FilteredSelectMultiple('Down Voted Posts', False),
        queryset=Post.objects.all(),
        required=False
    )
    down_voted_comments = forms.ModelMultipleChoiceField(
        widget=widgets.FilteredSelectMultiple('Down Voted Comments', False),
        queryset=Comment.objects.all(),
        required=False
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'new_password', 'first_name', 'last_name', 'age',
                'profile_pic', 'up_voted_posts', 'down_voted_posts', 'up_voted_comments',
                'down_voted_comments', 'is_active', 'is_staff', 'is_superuser', 'groups',
                'user_permissions', 'last_login', 'date_joined']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # TODO 💀
        self.fields['up_voted_posts'].queryset = Post.objects.all()
        self.fields['down_voted_posts'].queryset = Post.objects.all()
        self.fields['up_voted_comments'].queryset = Comment.objects.all()
        self.fields['down_voted_comments'].queryset = Comment.objects.all()
        self.fields['up_voted_posts'].initial = self.instance.up_voted_posts.all()
        self.fields['up_voted_posts'].initial = self.instance.down_voted_posts.all()
        self.fields['up_voted_comments'].initial = self.instance.up_voted_comments.all()
        self.fields['down_voted_comments'].initial = self.instance.down_voted_comments.all()

    def save(self, commit=True):
        res = super().save(commit)
        if self.cleaned_data.get('new_password'):
            self.instance.set_password(self.cleaned_data.get('new_password'))
        return res
