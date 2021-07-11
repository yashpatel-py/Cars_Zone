from django.contrib import admin
from django.utils.html import format_html
from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    # This fucntion will display all the images uploaded
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10%" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'
    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'price', 'body_style', 'fuel_type', 'is_features')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_features',)
    search_fields = ('car_title', 'id', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')

admin.site.register(Car, CarAdmin)