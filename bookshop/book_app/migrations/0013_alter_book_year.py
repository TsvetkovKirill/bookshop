# Generated by Django 4.2.4 on 2023-09-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0012_book_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="year",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
