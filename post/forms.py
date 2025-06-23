from django import forms
from django.contrib.admin import widgets

from .models import Post, Tag, Category


class PostAdminForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        widget=widgets.FilteredSelectMultiple('Tags', False),
        queryset=Tag.objects.all(),
        required=False
    )
    categories = forms.ModelMultipleChoiceField(
        widget=widgets.FilteredSelectMultiple('Categories', False),
        queryset=Category.objects.all(),
        required=False
    )
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'image', 'vote_up',
                    'vote_down', 'views', 'tags', 'categories']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.id:
            self.fields['tags'].queryset = Tag.objects.all()
            self.fields['categories'].queryset = Category.objects.all()
            self.fields['tags'].initial = self.instance.tags.all()
            self.fields['categories'].initial = self.instance.categories.all()
        else:
            self.fields['tags'].queryset = Tag.objects.all()
            self.fields['categories'].queryset = Category.objects.all()