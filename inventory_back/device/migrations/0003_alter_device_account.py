# Generated by Django 5.0.6 on 2024-05-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_device_account_alter_device_accounting_sum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='account',
            field=models.CharField(max_length=200, verbose_name='Счёт, субсчёт'),
        ),
    ]
