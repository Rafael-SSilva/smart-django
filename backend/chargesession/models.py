from django.db import models
from account.models import UserInfo


class ChargeSessionCost(models.Model):

    STATIONS = (
        ('A', 'Station A'),
        ('B', 'Station B'),
        ('C', 'Station C'),
    )

    user_info = models.ForeignKey(to=UserInfo, on_delete=models.CASCADE, blank=True, null=True)
    charge_datetime = models.DateTimeField(verbose_name='charge datetime' , auto_now_add=False)
    location = models.CharField(verbose_name='location' , max_length=1, choices=STATIONS)
    energy_kwh = models.DecimalField(verbose_name='energy kWh',  max_digits=10, decimal_places=2)
    cost = models.DecimalField(verbose_name='cost', max_digits=10, decimal_places=2)


    def __str__(self) -> str:
        return f'{self.user_info.first_name} - {self.location} - {self.charge_datetime}'