# Generated by Django 4.2 on 2023-08-29 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(verbose_name='phone'),
        ),
    ]
