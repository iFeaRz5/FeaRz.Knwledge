nama_pembeli = input("Masukkan Nama Pembeli: ")
kode_mainan = input("Masukkan Kode Mainan: ")
harga = int(input("Masukkan Harga: "))
jumlah_beli = int(input("Masukkan Jumlah Beli: "))

total = harga * jumlah_beli

print("---------------")
print("TOKO MAINAN ANAK")
print("---------------")
print(f"Nama Pembeli : {nama_pembeli}")
print(f"Kode Mainan  : {kode_mainan}")
print(f"Harga        : {harga}")
print(f"Jumlah Beli  : {jumlah_beli}")
print(f"Total        : {total}")