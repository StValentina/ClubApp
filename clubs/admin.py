from django.contrib import admin

from clubs.models import Club

# # Register your models here.
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'creator')
    search_fields = ('name', 'category')
    list_filter = ('category',)



