from django.db import models
from django.conf import settings


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    video = models.FileField(upload_to="videos/")
    processed_url = models.CharField(max_length=200, null=True)
    isProcessed = models.BooleanField(default=False)

    def __int__(self):
        return self.id

    # def __str__(self):
    #     return self.video.name


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="images/%d_%m_%Y/")
    processed_image = models.ImageField(upload_to="images/processed/%d_%m_%Y", null=True)

    def __int__(self):
        return self.id
