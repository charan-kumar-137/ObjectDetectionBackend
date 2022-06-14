from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from rest_framework.views import APIView
from .serializers import UserTokenObtainPairSerializer, UserSerializer
from django.contrib.auth.models import User


class ObtainTokenPairWithUserView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer


class UserCreate(APIView):
    """
    Creates a User based on the type given
    Either Student or Requester
    parameter
    ---------
    type : string
    data : JSON
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUser(APIView):

    def get(self, request):
        try:
            ret_user = User.objects.get(username=request.user)
            ret_user = UserSerializer(ret_user).data

            return Response(ret_user, status.HTTP_200_OK)
        except ObjectDoesNotExist:
            pass

        return Response({"ERR": "User Does not Exist"}, status.HTTP_404_NOT_FOUND)