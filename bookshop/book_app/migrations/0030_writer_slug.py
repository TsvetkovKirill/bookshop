# Generated by Django 4.2.4 on 2023-09-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0029_writer_full_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="writer",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
