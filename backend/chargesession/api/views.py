from rest_framework import generics

from chargesession.models import ChargeSessionCost
from chargesession.api.serializers import ChargeSessionSerializer
from system.Pagination import StandardPagination


class ListChargeSessions(generics.ListAPIView):
	queryset = ChargeSessionCost.objects.all().order_by('-charge_datetime')
	serializer_class = ChargeSessionSerializer
	pagination_class = StandardPagination
