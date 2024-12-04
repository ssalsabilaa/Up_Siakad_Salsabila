from django.db import models


class TahunAkademik(models.Model):
    # tahun
    # semester
    pass


# Create your models here.
class MataKuliah(models.Model):
    # nama
    # kode
    # prodi
    # sks
    pass


class Jadwal(models.Model):
    # nama
    # dosen
    # sks
    # jam_mulai
    # jam_selesai
    # semester
    pass


class KRS(models.Model):
    # tahun_akademik
    # mahasiswa
    # jadwal
    pass
