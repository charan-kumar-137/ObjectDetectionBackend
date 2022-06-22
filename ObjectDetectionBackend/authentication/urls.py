from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import ObtainTokenPairWithUserView, UserCreate, GetUser

urlpatterns = [
    path('user/create', UserCreate.as_view(), name="create_user"),
    path('token/create', ObtainTokenPairWithUserView.as_view(), name='token_create'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('user/get', GetUser.as_view(), name='get_user'),
]