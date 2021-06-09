from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    nama = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat_email = models.TextField()
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=3)
    nomor_hp = models.TextField()

class Agensi(models.Model):
    nama_agensi = models.TextField()
    deskripsi = models.TextField()

    def __str__(self):
        return '%s' (self.nama_agensi)   

class TourGuideProfile(models.Model):
    nama = models.ForeignKey(Profile, on_delete=models.CASCADE)
    jangkauan_harga = models.TextField()
    tempat_wisata = models.TextField()
    deskripsi = models.TextField()
    agensi = models.ForeignKey(Agensi, on_delete=models.CASCADE)

class Lokasi(models.Model):
    nama_tempat = models.TextField()
    deskripsi_tempat = models.TextField()

class Pesanan(models.Model):
    pelanggan = models.ForeignKey(User, on_delete=models.CASCADE)
    tour_guide = models.ForeignKey(TourGuideProfile, on_delete=models.CASCADE)
    lokasi = models.TextField()       