# Generated by Django 2.1.15 on 2021-06-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidemeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tanggal_lahir',
            field=models.DateField(),
        ),
    ]
