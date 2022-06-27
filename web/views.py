from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VideoSerializer, ImageSerializer
from django.contrib.auth.models import User
from .models import Video, Image
from django.core.exceptions import ObjectDoesNotExist


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


class ProcessVideo(APIView):

    def post(self, request, id):
        try:
            user = User.objects.get(username=request.user)
            video_obj = Video.objects.get(id=id, user=user)
            return Response("success", status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response("error", status.HTTP_400_BAD_REQUEST)


def detect_image():
    pass


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
