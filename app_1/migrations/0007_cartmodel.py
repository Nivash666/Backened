# Generated by Django 4.2.2 on 2023-07-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_1", "0006_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cartmodel",
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
                ("shop_image", models.CharField(max_length=1000)),
                ("shop_name", models.CharField(max_length=100)),
                ("product_image", models.CharField(max_length=1000)),
                ("product_name", models.CharField(max_length=100)),
                ("product_price", models.IntegerField()),
            ],
        ),
    ]
