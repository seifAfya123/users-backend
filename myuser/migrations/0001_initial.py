# Generated by Django 4.1.7 on 2023-02-23 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                (
                    "universty",
                    models.CharField(
                        choices=[
                            ("1", "cairo universty"),
                            ("2", "mansoura universty"),
                            ("3", "ECU"),
                        ],
                        max_length=20,
                        verbose_name="Universty",
                    ),
                ),
                (
                    "governrate",
                    models.CharField(
                        choices=[("1", "cairo"), ("2", "mansoura"), ("3", "alex")],
                        max_length=20,
                        verbose_name="Governrate",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User name",
                    ),
                ),
            ],
            options={"verbose_name": "user",},
        ),
    ]
