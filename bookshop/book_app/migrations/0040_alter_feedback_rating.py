# Generated by Django 4.2.4 on 2023-09-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0039_alter_feedback_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="rating",
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]
