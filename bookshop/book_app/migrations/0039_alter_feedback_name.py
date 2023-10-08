# Generated by Django 4.2.4 on 2023-09-18 18:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0038_alter_feedback_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="name",
            field=models.CharField(
                max_length=10, validators=[django.core.validators.MinLengthValidator(3)]
            ),
        ),
    ]
