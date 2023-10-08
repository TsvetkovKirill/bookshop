# Generated by Django 4.2.4 on 2023-09-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0013_alter_book_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="currency",
            field=models.CharField(
                choices=[("E", "Euro"), ("D", "Dollars"), ("R", "Rubles")],
                default="R",
                max_length=1,
            ),
        ),
    ]