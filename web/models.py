from django.db import models
from django.conf import settings


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.FileField(upload_to="videos/%d_%m_%Y/")

    def __int__(self):
        return self.id

    def __str__(self):
        return self.video.name
