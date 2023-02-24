from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.models import UserInfo

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.first_name

        return token
    

class UserInfoSeralizer(serializers.ModelSerializer):

  class Meta:
    model = UserInfo
    fields = ('id', 'email', 'first_name', 'last_name')
