# Generated by Django 5.2.1 on 2025-06-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hello",
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
                ("world", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "hello",
            },
        ),
    ]
