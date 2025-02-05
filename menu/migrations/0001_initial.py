# Generated by Django 4.2.18 on 2025-01-22 12:50

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Pizza', 'Pizza'), ('Pasta', 'Pasta'), ('Lasagna', 'Lasagna'), ('Starters', 'Starters'), ('Desserts', 'Desserts'), ('Drinks', 'Drinks'), ('Other', 'Other')], max_length=20)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', max_length=20)),
                ('publishing_status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1)),
            ],
        ),
    ]
