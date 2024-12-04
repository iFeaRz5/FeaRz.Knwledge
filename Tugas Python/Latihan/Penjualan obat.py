import pandas as pd

list_kode = []
list_nama = []
list_harga = []
list_jumlah = []
list_total = []

ulang = int(input("Banyaknya Jenis: "))
for i in range(ulang):
    print("Data Ke - " + str(i + 1))
    kode = input("Kode Obat (PD/PM/DD): ").upper()
    jumlah = int(input("Jumlah: "))

    if kode == "PD":
        nama = "Panadol"
        harga = 15000
    elif kode == "PM":
        nama = "Promag"
        harga = 20000
    elif kode == "DD":
        nama = "Bodrex"
        harga = 10000
    else:
        print("Kode Obat Tidak Ada, data tidak dimasukkan.")
        continue  

    list_kode.append(kode)
    list_nama.append(nama)
    list_harga.append(harga)
    list_jumlah.append(jumlah)
    list_total.append(harga * jumlah)


obat = {
    "Kode Obat": list_kode,
    "Nama Obat": list_nama,
    "Harga Satuan": list_harga,
    "Jumlah": list_jumlah,
    "Total Harga": list_total,
}

data_obat = pd.DataFrame(obat)


grand_total = data_obat["Total Harga"].sum()


print("==================== Daftar Obat =====================")
print(data_obat.to_string(index=False))  
print("=====================================================")
print(f"Total Keseluruhan Harga: Rp {grand_total:,}") 