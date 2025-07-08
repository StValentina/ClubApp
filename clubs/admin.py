from django.contrib import admin

# from clubs.models import Profile, Club, Event, Post, Comment
#
#
# # Register your models here.
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'avatar_url')
#     search_fields = ('user__username',)
#
# @admin.register(Club)
# class ClubAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'creator')
#     search_fields = ('name', 'category')
#     list_filter = ('category',)
#
# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ('title', 'club', 'date', 'location', 'creator')
#     list_filter = ('date', 'club',)
#     search_fields = ('title', 'location')
#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'club', 'author', 'created_on')
#     list_filter = ('club', 'created_on')
#     search_fields = ('title', 'content')
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('author', 'post', 'created_on')
#     list_filter = ('created_on',)
#     search_fields = ('author__username', 'text')


