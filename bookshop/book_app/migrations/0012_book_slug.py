# Generated by Django 4.2.4 on 2023-09-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0011_alter_book_is_best_selling"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
