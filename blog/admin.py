from django.contrib import admin
from blog.models import Tag, Post, Comment


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)
    list_display_links = ('tag_name',)
    search_fields = ('tag_name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'publish_date', 'active')
    list_display_links = ('publish_date', 'active')
    search_fields = ('post_title', 'publish_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile')
    list_display_links = ('id',)
    search_fields = ('id',)
