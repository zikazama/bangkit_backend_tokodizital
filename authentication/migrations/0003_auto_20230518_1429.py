# Generated by Django 3.2.19 on 2023-05-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20230518_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='authuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]