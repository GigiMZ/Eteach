from django.contrib import admin
from .models import Post, Comment, Tag


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ['author', 'content', 'comment', 'vote_up', 'vote_down', 'date']
    extra = 0

@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    list_display = ['title', 'author', 'date', 'views', 'vote_up', 'vote_down']
    readonly_fields = ['views']
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ['author', 'content_text', 'date', 'vote_up', 'vote_down']

    def content_text(self, obj):
        if len(obj.content) > 15: return obj.content[:15]+"..."
        return obj.content[:15]

    content_text.short_description = 'content'


admin.site.register(Tag)