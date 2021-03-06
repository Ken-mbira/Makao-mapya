# Generated by Django 3.2.8 on 2021-10-28 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_alter_house_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name_plural': 'Houses'},
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='houses/')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
            ],
            options={
                'verbose_name_plural': 'HouseImages',
            },
        ),
    ]
