# Generated by Django 2.2 on 2020-03-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ration', '0013_auto_20200315_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region_table',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]
