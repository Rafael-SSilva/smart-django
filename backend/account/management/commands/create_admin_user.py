import os
from django.db import transaction
from django.core.management.base import BaseCommand

from account.models import Account

ADMIN_EMAIL = os.environ.get('DJANGO_ADMIN_EMAIL', 'admin@email.com')
ADMIN_PASSWORD = os.environ.get('DJANGO_ADMIN_PASSWORD', 'admin@123')

class Command(BaseCommand):
    help = "Generates an admin user"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Creating admin user.")

        def create_user(email, first_name):
            print('email:',email)
            try:
                user = Account.objects.get(email=email)
            except:
                user = None
            
            if user is None:
                user = Account.objects.create(email=email, first_name=first_name)
            return user
        
        at_index = ADMIN_EMAIL.find("@")
        first_name = ADMIN_EMAIL[:at_index]
        
        admin_user = create_user(email=ADMIN_EMAIL, first_name=first_name)

        if admin_user is not None:
            admin_user.set_password(ADMIN_PASSWORD)
            admin_user.is_active = True
            admin_user.is_admin = True
            admin_user.is_staff = True
            admin_user.save()

            self.stdout.write("Admin user created/updated.")
        return
            
