from django.contrib import admin
from django.utils.html import format_html
from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):

    # This fucntion will display all the images uploaded
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10%" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('created_date', 'designation')

admin.site.register(Team, TeamAdmin)