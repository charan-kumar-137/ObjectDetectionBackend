from django.contrib import admin
from web.models import Video


class VideoAdmin(admin.ModelAdmin):
    model = Video


admin.site.register(Video, VideoAdmin)
