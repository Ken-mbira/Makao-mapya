# Generated by Django 3.2.8 on 2021-10-28 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0002_auto_20211028_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to=settings.AUTH_USER_MODEL),
        ),
    ]
