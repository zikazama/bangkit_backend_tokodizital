# Generated by Django 3.2.19 on 2023-05-18 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='is_staff',
        ),
    ]