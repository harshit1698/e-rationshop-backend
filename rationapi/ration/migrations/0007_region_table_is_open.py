# Generated by Django 2.2 on 2020-03-14 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ration', '0006_global_item_table_history_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='region_table',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
    ]
