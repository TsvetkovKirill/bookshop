# Generated by Django 4.2.4 on 2023-09-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_app", "0015_alter_book_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="year",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
