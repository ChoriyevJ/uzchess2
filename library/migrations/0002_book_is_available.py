# Generated by Django 4.2.7 on 2024-02-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
    ]
