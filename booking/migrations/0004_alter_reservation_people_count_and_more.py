# Generated by Django 4.2.18 on 2025-02-21 09:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_reservation_people_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='people_count',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='table_count',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
