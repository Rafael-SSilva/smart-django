from rest_framework import serializers

from chargesession.models import ChargeSessionCost
from account.api.serializers import UserInfoSeralizer

class ChargeSessionSerializer(serializers.ModelSerializer):
  user_info = UserInfoSeralizer()

  class Meta:
    model = ChargeSessionCost
    fields = ('id', 'charge_datetime', 'location', 'energy_kwh', 'cost', 'user_info')
    depth = 1

    