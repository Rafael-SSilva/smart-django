from django.db import transaction
from django.core.management.base import BaseCommand

from account.models import UserInfo

TOTAL_CUSTOMERS = 10

class Command(BaseCommand):
    help = "Generates dummy data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Cleaning up database.")

        UserInfo.objects.all().delete()

        def create_user_info(email, first_name, last_name):
            UserInfo.objects.create(email=email, first_name=first_name, last_name=last_name)

        #Create users
        for i in range(TOTAL_CUSTOMERS * 1):
            email = f'customer{i}@email.com'
            first_name = f'customer {i}'
            last_name = f'customer {i} last name'

            create_user_info(email, first_name, last_name)
        
        self.stdout.write("User infos gerenated successfully.")
