# Generated by Django 3.1.1 on 2020-10-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_auto_20201015_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='price_net_amount',
            field=models.DecimalField(decimal_places=2, default='5', max_digits=9),
        ),
    ]
