# Generated by Django 4.2.18 on 2025-01-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_reservation_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='people_count',
            field=models.PositiveIntegerField(default=4),
            preserve_default=False,
        ),
    ]
