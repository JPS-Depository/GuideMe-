# Generated by Django 2.1.15 on 2021-06-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidemeapp', '0004_auto_20210608_0347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agensi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_agensi', models.TextField()),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]