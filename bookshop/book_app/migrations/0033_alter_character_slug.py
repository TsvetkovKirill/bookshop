# Generated by Django 4.2.4 on 2023-09-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0032_character_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="slug",
            field=models.SlugField(blank=""),
        ),
    ]