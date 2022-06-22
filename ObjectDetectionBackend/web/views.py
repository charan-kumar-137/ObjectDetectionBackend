from io import BytesIO

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VideoSerializer, ImageSerializer
from django.contrib.auth.models import User
from .models import Video, Image
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import skimage.io
from PIL import Image as PILImage
from django.core.files.base import ContentFile
from detection.yolov5 import detect

model = settings.MODEL_OBJECT


class CreateVideo(APIView):

    def post(self, request):
        vid_serializer = VideoSerializer(data=request.FILES)
        if vid_serializer.is_valid():
            vid_obj = vid_serializer.create(vid_serializer.data)
            vid_obj.video = request.FILES.get('video')
            vid_obj.user = User.objects.get(username=request.user)
            vid_obj.save()

            return Response({"detail": "Success"}, status.HTTP_201_CREATED)

        return Response(vid_serializer.errors, status.HTTP_400_BAD_REQUEST)


class GetVideos(APIView):

    def get(self, request):
        user = User.objects.get(username=request.user)
        video_list = VideoSerializer(Video.objects.filter(user=user), many=True)

        return Response(video_list.data, status.HTTP_200_OK)


def detect_video(path=None):
    print(detect.run(source=path))


class ProcessVideo(APIView):

    def post(self, request):
        try:
            # print(request.POST)
            video_id = request.POST.get('id')
            user = User.objects.get(username=request.user)
            video_obj = Video.objects.get(id=video_id, user=user)
            detect_video('media/' + video_obj.video.name)
            video_obj.processed_url = 'media/' + 'videos/' + 'processed/' + video_obj.video.name.split('/')[-1]
            video_obj.isProcessed = True
            video_obj.save()
            return Response("success", status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response("error", status.HTTP_400_BAD_REQUEST)


class CreateImage(APIView):

    def post(self, request):
        img_serializer = ImageSerializer(data=request.FILES)
        if img_serializer.is_valid():
            img_obj = img_serializer.create(img_serializer.data)
            img_obj.image = request.FILES.get('image')
            img_obj.user = User.objects.get(username=request.user)
            img_obj.save()
            return Response({"detail": "Success"}, status.HTTP_201_CREATED)

        return Response(img_serializer.errors, status.HTTP_400_BAD_REQUEST)


class GetImages(APIView):

    def get(self, request):
        user = User.objects.get(username=request.user)
        image_list = ImageSerializer(Image.objects.filter(user=user), many=True)

        return Response(image_list.data, status.HTTP_200_OK)


class ProcessImage(APIView):
    def post(self, request):
        try:
            id = request.POST.get('id')
            user = User.objects.get(username=request.user)
            image_obj = Image.objects.get(id=id, user=user)
            img = PILImage.fromarray(model.detect([skimage.io.imread(image_obj.image)]))
            bio = BytesIO()
            img.save(bio, 'jpeg')
            image_obj.processed_image.save('test.jpg', ContentFile(bio.getvalue()))
            image_obj.save()
            return Response({"image": ''}, status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response("error", status.HTTP_400_BAD_REQUEST)


def download(request, id):
    if request.method == "POST":
        video_url = ''
        try:
            video_obj = Video.objects.get(id=id)
            video_url = '/media/' + 'videos/' + 'processed/' + video_obj.video.name.split('/')[-1]
        except ObjectDoesNotExist:
            pass
        return render(request, 'download.html', {'url': video_url})

    return render(request, 'download.html', {'id': id})
