# Generated by Django 4.2.4 on 2023-09-20 08:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0040_alter_feedback_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="rating",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MaxValueValidator(10)]
            ),
        ),
    ]
