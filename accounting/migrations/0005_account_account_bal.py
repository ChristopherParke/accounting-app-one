# Generated by Django 3.0.5 on 2020-04-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_item_newitemname'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_bal',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=25),
        ),
    ]
