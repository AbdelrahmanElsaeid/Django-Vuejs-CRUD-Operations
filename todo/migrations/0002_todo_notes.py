# Generated by Django 4.2.3 on 2023-07-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="notes",
            field=models.TextField(default="", max_length=300),
            preserve_default=False,
        ),
    ]