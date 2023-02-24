from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import Account


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email")