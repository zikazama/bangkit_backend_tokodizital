# Generated by Django 3.2.19 on 2023-05-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
