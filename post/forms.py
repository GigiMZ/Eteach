from django import forms
from .models import Post, Comment, Tag, Category
from django.contrib.admin import widgets


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

        self.fields['tags'].queryset = Tag.objects.all()
        self.fields['categories'].queryset = Category.objects.all()
        self.fields['tags'].initial = self.instance.tags.all()
        self.fields['categories'].initial = self.instance.categories.all()
