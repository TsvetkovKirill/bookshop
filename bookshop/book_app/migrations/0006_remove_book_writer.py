# Generated by Django 4.2.4 on 2023-09-01 09:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0005_alter_book_writer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="writer",
        ),
    ]
