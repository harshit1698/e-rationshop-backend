# Generated by Django 2.2.2 on 2020-03-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_table',
            name='contact_no',
            field=models.CharField(max_length=10),
        ),
    ]