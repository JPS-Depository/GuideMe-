# Generated by Django 2.1.15 on 2021-06-08 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidemeapp', '0007_lokasi_pesanan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='lokasi',
            field=models.TextField(),
        ),
    ]
