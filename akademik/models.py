from django.db import models


class TahunAkademik(models.Model):
    # tahun
    # semester
    pass


class MataKuliah(models.Model):
    # nama
    # kode
    # sks
    pass


class Jadwal(models.Model):
    # dosen
    # mata_kuliah
    # hari
    # jam_mulai
    # jam_selesai
    # ruang
    # kuota_peserta
    # tahun_akademik
    pass


class KRS(models.Model):
    # tahun_akademik
    # mahasiswa
    # jadwal
    pass
