from rest_framework import serializers
from .models import Video, Image


class VideoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    video = serializers.FileField(required=True)
    isProcessed = serializers.BooleanField(required=False)
    processed_url = serializers.CharField(required=False)

    class Meta:
        model = Video
        fields = ('id', 'video', 'isProcessed', 'processed_url')


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=True)
    processed_image = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = ('id', 'image', 'processed_image')
