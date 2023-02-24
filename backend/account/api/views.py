
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from account.models import UserInfo
from account.api.serializers import UserInfoSeralizer
from system.Pagination import StandardPagination

from account.api.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer

  def post(self, request, *args, **kwargs):
    user = None
    serializer = self.get_serializer(data=request.data)

    try:
        serializer.is_valid(raise_exception=True)
        user = serializer.user
    except TokenError as e:
        raise InvalidToken(e.args[0])
    
    return Response(serializer.validated_data, status=200)
  

class ListUsers(generics.ListAPIView):
    queryset = UserInfo.objects.all().order_by('email')
    serializer_class = UserInfoSeralizer
    pagination_class = StandardPagination