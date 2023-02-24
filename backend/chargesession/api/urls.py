from django.urls import path

from chargesession.api.views import ListChargeSessions

urlpatterns = [
    path('chargesession', ListChargeSessions.as_view(), name='list_chargesession'),
]
