from django.contrib import admin

from posts.models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'author', 'created_on')
    list_filter = ('club', 'created_on')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('author__username', 'text')