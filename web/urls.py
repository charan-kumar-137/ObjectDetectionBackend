from django.urls import path
from .views import CreateVideo, GetVideos, ProcessVideo, CreateImage, GetImages

urlpatterns = [
    path('video/create', CreateVideo.as_view(), name="create_video"),
    path('video/get', GetVideos.as_view(), name='get_videos'),
    path('video/process/<int:id>', ProcessVideo.as_view(), name='process_video'),
    path('image/create', CreateImage.as_view(), name='create_image'),
    path('image/get', GetImages.as_view(), name='get_images'),
]
