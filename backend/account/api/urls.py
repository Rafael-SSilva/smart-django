from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView
)

from account.api.views import CustomTokenObtainPairView

from account.api.views import ListUsers

urlpatterns = [
    path('auth/token', CustomTokenObtainPairView.as_view(), name='obtain_token'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='refresh_token'),
    path('auth/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('userinfo', ListUsers.as_view(), name='list_usersinfo'),
]
