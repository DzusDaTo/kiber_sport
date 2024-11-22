from django.contrib import admin
from .models import Stream


class StreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'is_live')
    search_fields = ('title',)
    list_filter = ('is_live',)


admin.site.register(Stream, StreamAdmin)

