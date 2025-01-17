# Generated by Django 5.1.1 on 2024-12-05 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=10, unique=True)),
                ('prodi', models.CharField(max_length=100)),
                ('sks', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TahunAkademik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun', models.CharField(max_length=9)),
                ('semester', models.CharField(choices=[('Ganjil', 'Ganjil'), ('Genap', 'Genap')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('dosen', models.CharField(max_length=100)),
                ('hari', models.CharField(choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')], max_length=10)),
                ('jam_mulai', models.TimeField()),
                ('jam_selesai', models.TimeField()),
                ('ruang', models.CharField(max_length=50)),
                ('kuota_peserta', models.PositiveIntegerField()),
                ('mata_kuliah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.matakuliah')),
                ('tahun_akademik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.tahunakademik')),
            ],
        ),
        migrations.CreateModel(
            name='KRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahasiswa', models.CharField(max_length=100)),
                ('jadwal', models.ManyToManyField(to='akademik.jadwal')),
                ('tahun_akademik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akademik.tahunakademik')),
            ],
        ),
    ]
