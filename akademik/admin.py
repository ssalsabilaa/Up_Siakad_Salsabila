from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import TahunAkademik, MataKuliah, Jadwal, KRS


@admin.register(TahunAkademik)
class TahunAkademikAdmin(admin.ModelAdmin):
    list_display = ("tahun", "semester")  # Menampilkan kolom ini di daftar admin
    list_filter = ("semester",)          # Menyediakan filter berdasarkan semester
    search_fields = ("tahun",)           # Menyediakan pencarian berdasarkan tahun


@admin.register(MataKuliah)
class MataKuliahAdmin(admin.ModelAdmin):
    list_display = ("kode", "nama", "prodi", "sks")
    list_filter = ("prodi",)             # Menyediakan filter berdasarkan program studi
    search_fields = ("kode", "nama")     # Menyediakan pencarian berdasarkan kode dan nama


@admin.register(Jadwal)
class JadwalAdmin(admin.ModelAdmin):
    list_display = ("nama", "dosen", "mata_kuliah", "hari", "jam_mulai", "jam_selesai", "ruang", "kuota_peserta", "tahun_akademik")
    list_filter = ("hari", "tahun_akademik", "mata_kuliah")  # Filter berdasarkan hari, tahun akademik, dan mata kuliah
    search_fields = ("nama", "dosen", "mata_kuliah__nama", "tahun_akademik__tahun")  # Pencarian
    autocomplete_fields = ("mata_kuliah", "tahun_akademik")  # Memudahkan input relasi ForeignKey


@admin.register(KRS)
class KRSAdmin(admin.ModelAdmin):
    list_display = ("mahasiswa", "tahun_akademik")  # Menampilkan mahasiswa dan tahun akademik
    list_filter = ("tahun_akademik",)               # Filter berdasarkan tahun akademik
    search_fields = ("mahasiswa", "tahun_akademik__tahun")  # Pencarian berdasarkan mahasiswa dan tahun akademik
    autocomplete_fields = ("tahun_akademik", "jadwal")      # Memudahkan input ManyToManyField
