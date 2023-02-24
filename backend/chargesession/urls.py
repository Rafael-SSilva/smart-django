
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('chargesession.api.urls'), name='chargesession-apis'),
]
