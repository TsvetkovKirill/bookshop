# Generated by Django 4.2.4 on 2023-09-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0016_book_genre_alter_book_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="currency",
            field=models.CharField(
                choices=[("EUR", "Euro"), ("USD", "Dollars"), ("RUB", "Rubles")],
                default="R",
                max_length=3,
            ),
        ),
    ]