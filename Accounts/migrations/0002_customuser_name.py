# Generated by Django 4.2 on 2023-08-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
