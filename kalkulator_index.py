nama_mahasiswa = input("Masukkan nama mahasiswa: ")
nilai_mat = float(input("Masukkan nilai matematika: "))
nilai_kim = float(input("Masukkana nilai kimia: "))
nilai_fis = float(input("Masukkkan nilai fisika: "))
nilai_berkom = float(input("Masukkan nilai berkom: "))

jumlah_nilai = nilai_mat * 3 + nilai_fis * 3 + nilai_kim * 3 + nilai_berkom * 3
indeks_akhir = jumlah_nilai / 12

print(f"[Mat]: {nilai_mat}; [Fisika]: {nilai_fis}; [Kimia]: {nilai_kim}; [Berkom]: {nilai_berkom}")
# Gimana kalau misalkan format output adalah "[Mat]: <nilai_mat>; [Fisika]: ..."

# Format: "Indeks akhir mahasiswa <nama_mahasiswa>: <indeks_akhir>"
print(f"Indeks akhir mahasiswa {nama_mahasiswa}: {indeks_akhir}")