# Generated by Django 3.1.1 on 2020-10-15 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20201015_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='origin',
            new_name='destination',
        ),
    ]