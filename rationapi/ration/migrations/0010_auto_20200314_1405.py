# Generated by Django 2.2 on 2020-03-14 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ration', '0009_request_region_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='is_accepted',
            new_name='is_reviewed',
        ),
    ]
