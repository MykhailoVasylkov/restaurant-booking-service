# Generated by Django 4.2.18 on 2025-01-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_menu_publishing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='publishing_status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]
