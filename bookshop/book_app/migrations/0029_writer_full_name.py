# Generated by Django 4.2.4 on 2023-09-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0028_book_publisher_house"),
    ]

    operations = [
        migrations.AddField(
            model_name="writer",
            name="full_name",
            field=models.CharField(default="not known", max_length=100),
        ),
    ]