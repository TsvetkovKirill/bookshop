# Generated by Django 4.2.4 on 2023-09-23 08:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0041_alter_feedback_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="name",
            field=models.CharField(
                max_length=30, validators=[django.core.validators.MinLengthValidator(3)]
            ),
        ),
    ]
