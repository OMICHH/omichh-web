from django.contrib import admin
from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ('title', 'type_event','date')
    list_display_links = ('title', 'type_event','date')
    search_fields = ('title', 'type_event','date')
    list_filter =  ('date',)
