# Code by 15210269 - Romadhan Edy Prasetyo

import helpers.main as helper

gaji_pokok = 300000
tunjangan_jabatan = 0
tunjangan_pendidikan = 0
honor_lembur = 0

print("---------------------------------------------")
print("\t\tPT INGIN DAMAI")
print("\tAplikasi Hitung Gaji Karyawan")
print("---------------------------------------------")

nama_karyawan = input("Nama Karyawan\t\t: ")

# Trycatch untuk form golongan jabatan
while True:
  try:
    golongan_jabatan = int(input("Golongan Jabatan\t: "))
    if golongan_jabatan == 1:
      tunjangan_jabatan = 0.05*gaji_pokok # 5% dari gaji pokok
      break
    elif golongan_jabatan == 2:
      tunjangan_jabatan = 0.10*gaji_pokok # 10% dari gaji pokok
      break
    elif golongan_jabatan == 3:
      tunjangan_jabatan = 0.15*gaji_pokok # 15% dari gaji pokok
      break
    else:
      print("Maaf, Golongan Jabatan hanya ada 1, 2, dan 3") # validasi jika user input data selain kondisi di atas
      continue
  except ValueError as err:
    print(err) # print jika terjadi error pada program

# Trycatch untuk form pendidikan
while True:
  try:
    pendidikan = input("Pendidikan\t\t: ")
    if pendidikan == "SMA":
      tunjangan_pendidikan = 0.025*gaji_pokok # 2.5% dari gaji pokok
      break
    elif pendidikan == "D1":
      tunjangan_pendidikan = 0.05*gaji_pokok # 5% dari gaji pokok
      break
    elif pendidikan == "D3":
      tunjangan_pendidikan = 0.20*gaji_pokok # 20% dari gaji pokok
      break
    elif pendidikan == "S1":
      tunjangan_pendidikan = 0.30*gaji_pokok # 30% dari gaji pokok
      break
    else:
      print("Maaf, Pendidikan hanya ada SMA, D1, D3 dan S1") # validasi jika user input data selain kondisi di atas
      continue
  except ValueError as err:
    print(err) # print jika terjadi error pada program

# Trycatch untuk form jumlah jam kerja
while True:
  try:
    jumlah_jam_kerja = int(input("Jumlah Jam Kerja\t: "))
    if jumlah_jam_kerja > 8:
      honor_lembur = (jumlah_jam_kerja-8)*3500
      break
    else:
      break
  except ValueError as err:
    print(err) # print jika terjadi error pada program

# Print the results
print("---------------------------------------------")
print("Karyawan yang bernama\t:", nama_karyawan)
print("\nHonor yang diterima\t")
print("Tunjangan Jabatan\t:", helper.currency(tunjangan_jabatan))
print("Tunjangan Pendidikan\t:", helper.currency(tunjangan_pendidikan))
print("Honor Lembur\t\t:", helper.currency(honor_lembur))
print("---------------------------------------------")
print("Total gaji\t\t:", helper.currency(gaji_pokok+tunjangan_jabatan+tunjangan_pendidikan+honor_lembur))
print("---------------------------------------------")