# Generated by Django 2.2 on 2020-03-15 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ration', '0011_auto_20200315_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='qualification',
        ),
        migrations.DeleteModel(
            name='Qualification',
        ),
    ]
