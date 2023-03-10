# Generated by Django 4.1.3 on 2022-12-23 03:54

# migracion inicial para trabajar con el modelo "entrada"
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bcrud", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entrada",
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
                ("titulo", models.CharField(max_length=100)),
                ("subtitulo", models.CharField(max_length=200)),
                ("texto", models.CharField(max_length=20000)),
            ],
        ),
    ]
