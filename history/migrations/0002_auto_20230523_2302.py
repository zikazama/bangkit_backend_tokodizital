# Generated by Django 3.2.19 on 2023-05-23 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='history',
            name='updated_at',
        ),
    ]
