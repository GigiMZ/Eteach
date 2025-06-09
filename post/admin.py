from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Post, Comment, Tag, Category
from .forms import PostAdminForm


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ['author', 'comment_link', 'vote_up',
                       'vote_down', 'date']
    exclude = ['comment']
    extra = 0

    def comment_link(self, obj):
        link = reverse("admin:post_comment_change", args=[obj.id])
        return format_html('<a href="{}">{}</a>', link, obj)

@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    list_display = ['title', 'author_link', 'post_categories', 'post_tags',
                    'date', 'views', 'vote_up', 'vote_down']

    readonly_fields = ['post_image_display', 'views', 'post_tags']

    form = PostAdminForm

    fieldsets = (
        ("Post", {
            'fields': ('author', 'title', 'content', 'post_image_display',
                       'image', ('vote_up', 'vote_down'), 'views')
        }),
        ("Category", {
            'fields': ('categories',)
        }),
        ("Tags", {
            'fields': ('tags',)
        }),
    )

    inlines = [CommentInline]

    def post_image_display(self, obj):
        if obj.image: return format_html(f'<img src="{obj.image.url}" width="200px"/>')

    def author_link(self, obj):
        link = reverse("admin:post_post_change", args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', link, obj.author)

    def post_tags(self, obj):
        if obj.tags: return ', '.join([tag.name for tag in obj.tags.all()])

    def post_categories(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])

    post_image_display.short_description = 'image'


@admin.register(Comment)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ['author', 'content_text', 'post_link', 'date', 'vote_up', 'vote_down']

    fieldsets = (
        ("Comment", {
            'fields': ('author', 'content', ('vote_up', 'vote_down'), 'post', 'comment')
        }),
    )

    def content_text(self, obj):
        if len(obj.content) > 15: return obj.content[:15]+"..."
        return obj.content[:15]

    def post_link(self, obj):
        link = reverse("admin:post_post_change", args=[obj.post.id])
        return format_html('<a href="{}">{}</a>', link, obj.post)

    content_text.short_description = 'content'


@admin.register(Tag)
class TagAdminModel(admin.ModelAdmin):
    list_display = ['name', 'posts_using']

    def posts_using(self, obj) -> int: return len(obj.posts.all())


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ['name', 'posts_using']

    def posts_using(self, obj) -> int: return len(obj.posts.all())
