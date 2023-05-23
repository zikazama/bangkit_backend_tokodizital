# Generated by Django 3.2.19 on 2023-05-23 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('history', '0003_auto_20230523_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='image',
            field=models.ImageField(upload_to=history.models.upload_to),
        ),
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.authuser'),
        ),
    ]
