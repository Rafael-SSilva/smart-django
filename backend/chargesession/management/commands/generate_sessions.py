from randomtimestamp import randomtimestamp 
from random import randint, uniform

from django.db import transaction
from django.core.management.base import BaseCommand

from account.models import UserInfo
from chargesession.models import ChargeSessionCost


TOTAL_SESSIONS_PER_USER = 50
STATIONS = ['A', 'B', 'C']
STATION_RATE = {'A': 6.83, 'B': 7.11, 'C': 9.74}

class Command(BaseCommand):
    help = "Generates charge sessions data"

    def generate_charge_sessions(self, user):

        def get_location() -> str:
            stations = STATIONS
            return stations[randint(0, 2)]

        
        def generate_consumption():
            return uniform(40.5, 100.0)

        
        def calculate_cost(localtion: str, kwh: float) -> float:
            base_rate = STATION_RATE
            localtion_rate = base_rate.get(localtion)
            cost = round(kwh * localtion_rate, 2)
            return cost


        user_info = user

        for i in range(TOTAL_SESSIONS_PER_USER+ 1):

            charge_datetime = randomtimestamp(start_year=2022, end_year=2022)
            location = get_location()
            energy_kwh = generate_consumption()
            cost = calculate_cost(location, energy_kwh)

            ChargeSessionCost.objects.create(
                user_info=user_info,
                charge_datetime=charge_datetime,
                location=location,
                energy_kwh=energy_kwh,
                cost=cost
            )


    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Cleaning up old sessions.")

        ChargeSessionCost.objects.all().delete()

        self.stdout.write("Sessions cleaned.")

        all_users = UserInfo.objects.all()

        for user in all_users:
            self.generate_charge_sessions(user)

        self.stdout.write("New charge sessions generated successfully.")

