from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": gettext_lazy("Invalid Credentials")
    }

    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)
        return token


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[
                                       UniqueValidator(User.objects.all(), message="Email Already Taken"),
                                   ])
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.username = instance.email
            instance.save()
        return instance
