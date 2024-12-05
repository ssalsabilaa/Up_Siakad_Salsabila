from django.db import models


class TahunAkademik(models.Model):
    tahun = models.CharField(max_length=9)  # Contoh format: "2024/2025"
    semester = models.CharField(max_length=10, choices=[("Ganjil", "Ganjil"), ("Genap", "Genap")])

    def __str__(self):
        return f"{self.tahun} - {self.semester}"


class MataKuliah(models.Model):
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=10, unique=True)
    prodi = models.CharField(max_length=100)  # Program Studi
    sks = models.PositiveIntegerField()  # Satuan Kredit Semester

    def __str__(self):
        return f"{self.kode} - {self.nama}"


class Jadwal(models.Model):
    nama = models.CharField(max_length=100)
    dosen = models.CharField(max_length=100)  # Nama dosen
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    hari = models.CharField(
        max_length=10, 
        choices=[
            ("Senin", "Senin"), 
            ("Selasa", "Selasa"), 
            ("Rabu", "Rabu"), 
            ("Kamis", "Kamis"), 
            ("Jumat", "Jumat"), 
            ("Sabtu", "Sabtu"), 
            ("Minggu", "Minggu")
        ]
    )
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    ruang = models.CharField(max_length=50)
    kuota_peserta = models.PositiveIntegerField()
    tahun_akademik = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nama} - {self.hari} {self.jam_mulai}-{self.jam_selesai}"


class KRS(models.Model):
    tahun_akademik = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE)
    mahasiswa = models.CharField(max_length=100)  # Nama atau ID mahasiswa
    jadwal = models.ManyToManyField(Jadwal)

    def __str__(self):
        return f"KRS {self.mahasiswa} - {self.tahun_akademik}"
