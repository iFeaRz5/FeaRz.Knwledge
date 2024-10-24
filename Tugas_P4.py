print("===========================================================")
print("                   Tiket Bus Bekasi Kota                   ")
print("===========================================================")
nama = input("Masukan Nama Pembeli: ")
jumlah_beli = int(input("Masukan Jumlah Tiket yang akan dibeli: "))
no_hp = input("Masukan No HP: ")
kode_jurusan = input("Masukan Kode Jurusan [SBY/BL/LMP]: ")

# Data harga tiket
harga_tiket = {
    "SBY": 300000,
    "BL": 350000,
    "LMP": 500000
}

# Nama kota berdasarkan kode jurusan
nama_kota = {
    "SBY": "Surabaya",
    "BL": "Bali",
    "LMP": "Lampung"
}

# Menghitung potongan
if jumlah_beli >= 3:
    potongan = 0.1  # 10% discount
else:
    potongan = 0

# Menghitung total harga
if kode_jurusan in harga_tiket:
    harga = harga_tiket[kode_jurusan]
    total_harga = (jumlah_beli * harga) * (1 - potongan)
else:
    harga = 0
    total_harga = 0
    print("Kode jurusan yang anda masukan salah!")

if total_harga > 0:
    print("===========================================================")
    print("         Detail Pembayaran Tiket Bus Bekasi Kota           ")
    print("===========================================================")
    print("Nama Pembeli: " + nama)
    print("No HP: " + no_hp)
    print("Jurusan: " + nama_kota[kode_jurusan])
    print("Harga Tiket: Rp.", harga)
    print("Jumlah Beli: ", jumlah_beli)
    print("Potongan: Rp.", potongan * harga * jumlah_beli)
    print("Total Harga: Rp.", total_harga)
else:
    print("Tidak ada harga karena inputan salah.")
    
jumlah_bayar= int(input("Masukan Uang Bayar : Rp-"))
kembalian= jumlah_bayar - total_harga
if jumlah_bayar >= total_harga :
     print("Kembali: Rp. ",+kembalian )
     print("===========================================================")
     print("        Terima Kasih Telah Menggunakan Jasa kami 😊        ")
     print("===========================================================")
else :
     print("Uang Anda Tidak Cukup")
     print("===========================================================")
     print("        Terima Kasih Telah Menggunakan Jasa kami 😊       ")
     print("===========================================================")