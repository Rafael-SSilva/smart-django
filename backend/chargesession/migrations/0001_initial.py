# Generated by Django 4.1.7 on 2023-02-23 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargeSessionCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_datetime', models.DateTimeField(verbose_name='charge datetime')),
                ('location', models.CharField(choices=[('A', 'Station A'), ('B', 'Station B'), ('C', 'Station C')], max_length=1, verbose_name='location')),
                ('energy_kwh', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='energy kWh')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cost')),
                ('user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userinfo')),
            ],
        ),
    ]
