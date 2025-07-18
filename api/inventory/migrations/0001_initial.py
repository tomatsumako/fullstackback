# Generated by Django 5.2.1 on 2025-07-11 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100, verbose_name="商品名")),
                ("price", models.IntegerField(verbose_name="価格")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="商品説明"),
                ),
            ],
            options={
                "verbose_name": "商品",
                "db_table": "product",
            },
        ),
        migrations.CreateModel(
            name="Purchase",
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
                ("quantity", models.IntegerField(verbose_name="数量")),
                ("purchase_date", models.DateTimeField(verbose_name="仕入日時")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "仕入",
                "db_table": "purchase",
            },
        ),
        migrations.CreateModel(
            name="Sales",
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
                ("quantity", models.IntegerField(verbose_name="数量")),
                ("sales_date", models.DateTimeField(verbose_name="売上日時")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "売上",
                "db_table": "sales",
            },
        ),
    ]
