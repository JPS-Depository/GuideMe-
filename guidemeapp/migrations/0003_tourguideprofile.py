# Generated by Django 2.1.15 on 2021-06-07 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guidemeapp', '0002_auto_20210608_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourGuideProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alamat_email', models.TextField()),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.CharField(max_length=3)),
                ('jangkauan_harga', models.TextField()),
                ('tempat_wisata', models.TextField()),
                ('deskripsi', models.TextField()),
                ('agensi', models.TextField()),
                ('nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guidemeapp.Profile')),
            ],
        ),
    ]
