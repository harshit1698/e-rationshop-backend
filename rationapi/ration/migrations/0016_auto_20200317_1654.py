# Generated by Django 2.2 on 2020-03-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ration', '0015_monthly_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_rating',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]