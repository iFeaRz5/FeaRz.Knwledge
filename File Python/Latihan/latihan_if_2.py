kode_baju = input("Masukan Kode Baju [SP/AD] : ")
ukuran = input("Masukan Ukuran Baju [S/M] : ")

brands = {
    "SP": "SuperDry",
    "AD": "Adidas"
}

prices = {
    "SP": {"S": 450000, "M": 500000},
    "AD": {"S": 650000, "M": 700000}
}

kode_baju = kode_baju.upper()
ukuran = ukuran.upper()

if kode_baju in brands and ukuran in prices[kode_baju]:
    merk = brands[kode_baju]
    harga = prices[kode_baju][ukuran]
else:
    merk = "Anda Salah Input Kode Merk"
    harga = 0

print("-----------------------------")
print("Merk Baju : " + merk)
print("Harga Baju : Rp.", harga)