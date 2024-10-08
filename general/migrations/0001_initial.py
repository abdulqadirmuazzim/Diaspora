# Generated by Django 5.0.4 on 2024-08-27 21:18

import datetime
import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=255)),
                ("Email", models.EmailField(max_length=255)),
                (
                    "Phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("Address", models.CharField(max_length=300)),
                ("Message", models.TextField()),
                (
                    "date_created",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024,
                            8,
                            27,
                            21,
                            18,
                            41,
                            896258,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("SubEmail", models.EmailField(max_length=255)),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
