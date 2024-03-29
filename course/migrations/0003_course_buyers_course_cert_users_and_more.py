# Generated by Django 4.2.7 on 2024-02-13 14:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("course", "0002_alter_lesson_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="buyers",
            field=models.ManyToManyField(related_name="buy_courses", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="course",
            name="cert_users",
            field=models.ManyToManyField(related_name="certificated_courses", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="lesson",
            name="finished_users",
            field=models.ManyToManyField(related_name="finished_lessons", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="course",
            name="likes",
            field=models.ManyToManyField(related_name="like_courses", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name="chapter",
            unique_together={("title", "course")},
        ),
    ]
