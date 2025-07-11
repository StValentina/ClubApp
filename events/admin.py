from django.contrib import admin

from events.models import Event


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'date', 'location', 'creator')
    list_filter = ('date', 'club',)
    search_fields = ('title', 'location')