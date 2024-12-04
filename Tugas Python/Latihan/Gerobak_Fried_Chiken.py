print("          GEROBAK FRIED CHIKEN            ")
print("==========================================")
print("KODE       JENIS POTONG             HARGA ")
print("  D            Dada                 2500  ")
print("  P            Paha                 2000  ")
print("  S            Sayap                1500  ")
print("==========================================")

ulang = int(input("Banyaknya Jenis : "))

rincian_pembelian = []
total_harga = 0

for i in range(ulang):
    print("Jenis Ke - " + str(i + 1)) 
    kode = input("Kode Potong [D/P/S]: ").upper()
    jumlah = int(input("Banyak Potong : "))
    
    if kode == "D":
        nama = "Dada "
        harga = 2500
    elif kode == "P":
        nama = "Paha "
        harga = 2000
    elif kode == "S":
        nama = "Sayap"
        harga = 1500
    else:
        print("Makanan tidak tersedia.")
        continue  
    
    jumlah_harga = harga * jumlah
    rincian_pembelian.append((i + 1, nama, harga, jumlah, jumlah_harga))
    total_harga += jumlah_harga
    
    print("")  

print("               GEROBAK FRIED CHICKEN")
print("---------------------------------------------------------")
print("No  Jenis Potong  Harga Satuan  Banyak Beli  Jumlah Harga")
print("---------------------------------------------------------")

for item in rincian_pembelian:
    no, jenis, harga_satuan, banyak_beli, jumlah_harga = item
    print(f"{no}      {jenis}          Rp {harga_satuan}            {banyak_beli}          Rp {jumlah_harga}")

print("---------------------------------------------------------")
pajak = total_harga * 0.1
total_bayar = total_harga + pajak
print(f"                                   Jumlah Bayar    Rp {total_harga}")
print(f"                                   Pajak 10%       Rp {pajak}      ")
print(f"                                   Total Bayar     Rp {total_bayar}")
print("Kasir : Desta Yoga pratama dan Muhammad Dauddy Ibrahim              ")