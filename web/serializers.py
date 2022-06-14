from rest_framework import serializers
from .models import Video, Image


class VideoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    video = serializers.FileField(required=True)
    isProcessed = serializers.BooleanField(required=False)

    class Meta:
        model = Video
        fields = ('id', 'video', 'isProcessed')


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=True)

    class Meta:
        model = Image
        fields = ('id', 'image')
