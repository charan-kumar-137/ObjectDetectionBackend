from django.contrib import admin
from web.models import Video, Image


class VideoAdmin(admin.ModelAdmin):
    model = Video


class ImageAdmin(admin.ModelAdmin):
    model = Image


admin.site.register(Video, VideoAdmin)
admin.site.register(Image, ImageAdmin)
