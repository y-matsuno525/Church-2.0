# Generated by Django 5.1 on 2024-11-20 04:59

import mdeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dogmatics", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preprint",
            name="content",
            field=mdeditor.fields.MDTextField(),
        ),
    ]
