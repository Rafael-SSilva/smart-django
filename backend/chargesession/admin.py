from django.contrib import admin
from chargesession.models import ChargeSessionCost

class ChargeSessionAdmin(admin.ModelAdmin):
    list_display = ('user_info', 'charge_datetime', 'location', 'energy_kwh', 'cost')
    list_filter = ("location",)
    search_fields = ("location",)
    ordering = ("charge_datetime", )
    list_per_page = 15
    

admin.site.register(ChargeSessionCost, ChargeSessionAdmin)