from datetime import datetime


data_pengguna = {
    "234567": {"pin": 918918, "saldo": 1000000, "nama": "Muhammad Brimstone"},
    "992299": {"pin": 458458, "saldo": 580000, "nama": "Slamet Kopling"},
    "237788": {"pin": 765765, "saldo": 200000, "nama": "Samsul Arip"}
}

tagihan_data = {
    "ABC123": {"nama": "PLN", "jumlah": 150000},
    "DEF456": {"nama": "Netlix", "jumlah": 100000},
    "GHI789": {"nama": "Indihome", "jumlah": 200000},
}

bahasa = {}

def format_rupiah(amount):
    return "Rp {:,}".format(amount).replace(",", ".")

def cetak_struk(aksi, nominal, saldo_akhir, nama_tujuan=None):
    waktu_transaksi = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    print("")
    print("------------------------------------------------------")
    print("")
    if bahasa["bahasa_dipilih"] == "Bahasa Indonesia dipilih.":
        print("                STRUK TRANSAKSI ATM BSS                  ")
        print("")
        print(f" Waktu Transaksi : {waktu_transaksi}")
        print(f" Jenis Transaksi : {aksi}")
        print(f" Nominal         : {format_rupiah(nominal)}")
        print(f" Saldo Akhir     : {format_rupiah(saldo_akhir)}")
    else:
        print("                ATM BSS TRANSACTION RECEIPT              ")
        print("")
        print(f" Transaction Time : {waktu_transaksi}")
        print(f" Transaction Type : {aksi}")
        print(f" Amount           : {format_rupiah(nominal)}")
        print(f" Remaining Balance: {format_rupiah(saldo_akhir)}")
    print("")
    print("------------------------------------------------------")
    print("")



def cek_saldo(nomor_rekening):
    if nomor_rekening in data_pengguna:
        print("")
        print("******************************************************")
        print("")
        print(f"       {bahasa['saldo_anda']}", format_rupiah(data_pengguna[nomor_rekening]["saldo"]))
        print("")
        print("******************************************************")
        print("")
    else:
        print("")
        print("\033[31m" + bahasa['rekening_tidak_ada'] + "\033[0m")
        print("")



def transfer(nomor_rekening_pengirim, nomor_rekening_tujuan, jumlah):
    
    if nomor_rekening_pengirim in data_pengguna and nomor_rekening_tujuan in data_pengguna:

        nama_tujuan = data_pengguna[nomor_rekening_tujuan]["nama"]
        print("")
        print(f"        {bahasa['Nama_Rekening_Tujuan']} {nama_tujuan}")
        print("")
        
        
        konfirmasi = input(bahasa["lanjut_transfer"]).lower()
        if konfirmasi == "y":
            
            if data_pengguna[nomor_rekening_pengirim]["saldo"] >= jumlah:
                data_pengguna[nomor_rekening_pengirim]["saldo"] -= jumlah
                data_pengguna[nomor_rekening_tujuan]["saldo"] += jumlah
                print("")
                print("******************************************************")
                print("")
                print("\033[32m" +f"         {bahasa['Transfer_Berhasil']}" + "\033[0m" )
                print(f"         {bahasa['sisa_saldo_anda']}", format_rupiah(data_pengguna[nomor_rekening_pengirim]["saldo"]))
                print("")
                print("******************************************************")
                print("")
                
               
                if input(bahasa["ingin_cetak_struk"]).lower() == "y":
                    cetak_struk(bahasa["transfer"], jumlah, data_pengguna[nomor_rekening_pengirim]["saldo"])

            else:
                print("")
                print("\033[31m" + bahasa["saldo_kurang"] + "\033[0m")
        else:
            print("")
            print("\033[31m" + bahasa['transfer_batal'] + "\033[0m")
            print("")
    else:
        print("")
        print("\033[31m" + bahasa['rekening_tidak_ada'] + "\033[0m")
        print("")





def tarik_tunai(nomor_rekening):
    if nomor_rekening in data_pengguna:
        print("******************************************************")
        print("")
        print(f"                     {bahasa['pilih_nominal']}                    ")
        print("")
        print("******************************************************")
        print("")
        print("1. Rp 100.000")
        print("2. Rp 200.000")
        print("3. Rp 500.000")
        print("4. Rp 1.000.000")
        print("5. Rp 2.000.000")
        print(f"6. {bahasa['nominal_lain']}")
        print("")

        pilihan_nominal = input(bahasa["input_nominal"])
        if pilihan_nominal == "1":
            jumlah = 100000
        elif pilihan_nominal == "2":
            jumlah = 200000
        elif pilihan_nominal == "3":
            jumlah = 500000
        elif pilihan_nominal == "4":
            jumlah = 1000000
        elif pilihan_nominal == "5":
            jumlah = 2000000
        elif pilihan_nominal == "6":
            jumlah = int(input(bahasa["masukan_jumlah_tarik"]))
        else:
            print("")
            print("\033[31m" + bahasa["pilihan_valid"] + "\033[0m" )
            print("")
            return

        if data_pengguna[nomor_rekening]["saldo"] >= jumlah:
            data_pengguna[nomor_rekening]["saldo"] -= jumlah
            print("")
            print("******************************************************")
            print("")
            print("\033[32m" + f"        {bahasa['penarikan_berhasil']}" + "\033[0m")
            print(f"        {bahasa['sisa_saldo_anda']}", format_rupiah(data_pengguna[nomor_rekening]["saldo"]))
            print("")
            print("******************************************************")
            print("")
            
            
            if input(bahasa["ingin_cetak_struk"]).lower() == "y":
                cetak_struk(bahasa["tarik_tunai"], jumlah, data_pengguna[nomor_rekening]["saldo"])

        else:
            print("")
            print("\033[31m" + bahasa["saldo_kurang"] + "\033[0m" )
            print("")
    else:
        print("")
        print("\033[31m" + bahasa["rekening_tidak_ada"] + "\033[0m")
        print("")




def ganti_pin(nomor_rekening):
    if nomor_rekening in data_pengguna:
        pin_baru = int(input(bahasa["masukan_pin_baru"]))
        data_pengguna[nomor_rekening]["pin"] = pin_baru
        print("")
        print("\033[32m" + bahasa["pin_berhasil_diubah"] + "\033[0m")
        print("")
    else:
        print("")
        print("\033[31m" + bahasa["rekening_tidak_ada"] + "\033[0m")
        print("")




def riwayat(nomor_rekening):
    if nomor_rekening in data_pengguna:
        transactions = [
            f"25/10/2024 - {bahasa['tarik_tunai2']} Rp 1.000.000",
            f"23/10/2024 - {bahasa['transfer']} Rp 500.000",
            f"21/10/2024 - {bahasa['setor_tunai']} Rp 2.000.000",
        ]
        print("******************************************************")
        print("")
        print(f"                   {bahasa['riwayat']}")
        for transaction in transactions:
            print(transaction)
        print("")
        print("******************************************************")
    else:
        print("")
        print("\033[31m" + bahasa["rekening_tidak_ada"] + "\033[0m")
        print("")





def bayar_tagihan(nomor_rekening):
    kode_bayar = input(bahasa["kode_bayar"])
    if kode_bayar in tagihan_data:
        tagihan = tagihan_data[kode_bayar]
        print("")
        print("******************************************************")
        print("")
        print(f"        {tagihan['nama']}")
        print(f"        {bahasa['jumlah_tagihan']}{format_rupiah(tagihan['jumlah'])}")
        print("")
        print("******************************************************")
        print("")
        konfirmasi = input(bahasa["bayar_tagihan_confirm"]).lower()
        if konfirmasi == "y":
            if data_pengguna[nomor_rekening]["saldo"] >= tagihan["jumlah"]:
                data_pengguna[nomor_rekening]["saldo"] -= tagihan["jumlah"]
                print("")
                print("******************************************************")
                print("")
                print("\033[32m" + f"        {bahasa['pembayaran_berhasil']}" "\033[0m")
                print(f"        {bahasa['sisa_saldo']}", format_rupiah(data_pengguna[nomor_rekening]["saldo"]))
                print("")
                print("******************************************************")
                print("")
                
                
                if input(bahasa["ingin_cetak_struk"]).lower() == "y":
                    cetak_struk(bahasa["bayar_tagihan"], tagihan["jumlah"], data_pengguna[nomor_rekening]["saldo"])

            else:
                print("")
                print("\033[31m" + bahasa["saldo_kurang"] + "\033[0m")
                print("")
        else:
            print("")
            print("\033[31m" + bahasa["pembayaran_batal"] + "\033[0m")
            print("")
    else:
        print("")
        print("\033[31m" + bahasa["kode_bayar_tidak_ada"] + "\033[0m")
        print("")




def show_help():
    print("")
    print("==============================================================")
    print(f"                    {bahasa['bantuan']}                             ")
    print("==============================================================")
    print("")
    print(f"1. {bahasa['bantuan1']}")
    print(f"2. {bahasa['bantuan2']}")
    print(f"3. {bahasa['bantuan3']}")
    print(f"4. {bahasa['bantuan4']}")
    print(f"5. {bahasa['bantuan5']}")
    print(f"7. {bahasa['bantuan7']}")
    print(f"8. {bahasa['bantuan8']}")
    print("")
    print("==============================================================")
    print("")





def set_bahasa():
    global bahasa
    print("Pilih Bahasa:")
    print("1. Bahasa Indonesia")
    print("2. English")
    pilihan_bahasa = input("Pilih (1/2): ")

    if pilihan_bahasa == "1":
        bahasa = {
            "bahasa_dipilih": "Bahasa Indonesia dipilih.",
            "masukkan_rekening": "Masukkan Nomor Rekening : ",
            "masukkan_pin": "Masukkan Pin Anda : ",
            "pilih_menu": "Pilih Menu",
            "cek_saldo": "Cek Saldo     ",
            "transfer": "Transfer Uang",
            "tarik_tunai": "Tarik Tunai     ",
            "tarik_tunai2": "Tarik Tunai",
            "ganti_pin": "Ganti PIN     ",
            "riwayat": "Riwayat",
            "bantuan": "Bantuan",
            "bayar_tagihan": "Bayar Tagihan",
            "keluar": "Keluar",
            "kode_bayar": "Masukkan Kode Bayar : ",
            "jumlah_tagihan": "Jumlah Tagihan : ",
            "bayar_tagihan_confirm": "Apakah Anda ingin membayar tagihan ini? (y/n): ",
            "pembayaran_berhasil": "Pembayaran Berhasil",
            "sisa_saldo": "Sisa Saldo Anda : ",
            "transaksi_lain": "Apakah ingin melakukan transaksi lain? (y/n): ",
            "login_sukses": "Login berhasil.",
            "login_gagal": "Nomor Rekening atau Pin Anda Salah.",
            "saldo_anda": "Saldo Anda : ",
            "Masukkan_Nomor_Rekening_Tujuan": " Masukan Nomor Rekening Tujuan : ",
            "Masukkan_Jumlah_Transfer": " Masukan Jumlah Transfer : ",
            "Nama_Rekening_Tujuan": "Nama Rekening Tujuan :",
            "lanjut_transfer": " Apakah Anda ingin melanjutkan transfer ini? (y/n): ",
            "Transfer_Berhasil": "Transfer Berhasil",
            "sisa_saldo_anda": "Sisa Saldo Anda : ",
            "ingin_cetak_struk": " Apakah Anda ingin mencetak struk? (y/n) : ",
            "nominal_lain": "Nominal Lainnya",
            "input_nominal": " Pilih Nominal (1-5): ",
            "masukan_jumlah_tarik": "Masukkan Jumlah Penarikan : ",
            "penarikan_berhasil": "Penarikan Berhasil",
            "masukan_pin_baru": " Masukan PIN Baru : ",
            "pin_berhasil_diubah": " PIN Berhasil Diubah.",
            "setor_tunai": "Setor Tunai",
            "bantuan1": "Cek Saldo - Cek rekening anda.",
            "bantuan2": "Transfer Uang - Mengirim uang ke rekening lain.",
            "bantuan3": "Tarik Tunai - Tarik tunai dari rekening anda.",
            "bantuan4": "Ganti PIN - Ganti PIN akun anda.",
            "bantuan5": "Riwayat - Melihat seluruh riwayat transaksi rekening anda.",
            "bantuan7": "Bayar Tagihan - Bayar Tagihan Rekening Anda.",
            "bantuan8": "Keluar - Keluar dari ATM.",
            "pilih_nominal": "Pilih Nominal",
            "rekening_tidak_ada": "Rekening Tidak ditemukan.",
            "saldo_kurang": " Saldo Anda Tidak Mencukupi",
            "transfer_batal": "Transfer Dibatalkan",
            "pembayaran_batal": "Pembayaran Dibatalkan",
            "kode_bayar_tidak_ada": "Kode Bayar Tidak Ditemukan",
            "pilihan_valid": "Pilihan Tidak Valid",
            "trmksh_menggunakan_atm": "Terimakasih Telah Menggunakan ATM BSS"
        }
    elif pilihan_bahasa == "2":
        bahasa = {
            "bahasa_dipilih": "English selected.",
            "masukkan_rekening": "Enter Account Number : ",
            "masukkan_pin": "Enter Your PIN : ",
            "pilih_menu": "Select Menu",
            "cek_saldo": "Check Balance  ",
            "transfer": "Money Transfer",
            "tarik_tunai": "Withdraw         ",
            "tarik_tunai2": "Withdraw",
            "ganti_pin": "Change PIN     ",
            "riwayat": "History",
            "bantuan": "Help",
            "bayar_tagihan": "Pay Bill",
            "keluar": "Exit",
            "kode_bayar": "Enter Payment Code : ",
            "jumlah_tagihan": "Bill Amount : ",
            "bayar_tagihan_confirm": "Do you want to pay this bill? (y/n): ",
            "pembayaran_berhasil": "Payment Successful",
            "sisa_saldo": "Your Remaining Balance : ",
            "transaksi_lain": "Do you want to make another transaction? (y/n): ",
            "login_sukses": "Login successful.",
            "login_gagal": "Account Number or PIN is incorrect.",
            "saldo_anda": "Your Balance : ",
            "Masukkan_Nomor_Rekening_Tujuan": " Enter the Destination Account Number : ",
            "Masukkan_Jumlah_Transfer": " Enter the Transfer Amount : ",
            "Nama_Rekening_Tujuan": "Destination Account Name :",
            "lanjut_transfer": " Do you want to continue with this transfer? (y/n): ",
            "Transfer_Berhasil": "Transfer Successful",
            "sisa_saldo_anda": "Your Remaining Balance : ",
            "ingin_cetak_struk": " Do you want to print a receipt? (y/n) : ",
            "nominal_lain": "Other Nominal",
            "input_nominal": "Select Nominal (1-5) : ",
            "masukan_jumlah_tarik": "Enter Withdrawal Amount : ",
            "penarikan_berhasil": "Withdrawal Successful",
            "masukan_pin_baru": " Enter a New PIN : ",
            "pin_berhasil_diubah": " PIN Changed Successfully.",
            "setor_tunai": "Deposit",
            "bantuan1": "Check Balance - Check your account.",
            "bantuan2": "Money Transfer - Send money to another account.",
            "bantuan3": "Cash Withdrawal - Withdraw cash from your account.",
            "bantuan4": "Change PIN - Change your account PIN.",
            "bantuan5": "History - View your entire account transaction history.",
            "bantuan7": "Pay Bills - Pay Your Account Bills.",
            "bantuan8": "Exit - Exit the ATM.",
            "pilih_nominal": "Select Nominal",
            "rekening_tidak_ada": "Account Not found.",
            "saldo_kurang": " Your Balance is Insufficient",
            "transfer_batal": "Transfer Canceled",
            "pembayaran_batal": "Payment Canceled",
            "kode_bayar_tidak_ada": "Payment Code Not Found",
            "pilihan_valid": "Invalid Choice",
            "trmksh_menggunakan_atm": "Thank you For Using BSS ATM"        
        }
    else:
        print("")
        print("\033[31m" + "Pilihan tidak valid. Default ke Bahasa Indonesia." + "\033[0m")
        print("")
        set_bahasa()

def transaksi_lagi():
    pilihan = input(bahasa["transaksi_lain"]).lower()
    return pilihan == "y"

def main():
    print("==============================================================")
    print("                  Selamat Datang di ATM BSS                   ")
    print("==============================================================")
    set_bahasa()
    print("")
    print("\033[32m" + bahasa["bahasa_dipilih"] + "\033[0m")
    print("")
    
    nomor_rekening = input(bahasa["masukkan_rekening"] + " ")
    pin = input(bahasa["masukkan_pin"] + " ")
    print("")

    if nomor_rekening == "" or pin == "" or not pin.isnumeric():
        print("\033[31m" + bahasa["login_gagal"] + "\033[0m")
        return False
    else:
        pin = int(pin)
    
    if nomor_rekening in data_pengguna and data_pengguna[nomor_rekening]["pin"] == pin:
        print("\033[32m" + bahasa["login_sukses"] + "\033[0m")
        while True:
            print("")
            print("==============================================================")
            print(f"                         {bahasa['pilih_menu']}                           ")
            print("==============================================================")
            print(f"(1). {bahasa['cek_saldo']}                              (5). {bahasa['riwayat']}")
            print(f"(2). {bahasa['transfer']}                               (6). {bahasa['bantuan']}")
            print(f"(3). {bahasa['tarik_tunai']}                            (7). {bahasa['bayar_tagihan']}")
            print(f"(4). {bahasa['ganti_pin']}                              (8). {bahasa['keluar']}")
            print("")
            pilihan = input(bahasa["pilih_menu"] + " (1-8): ")
            print("")

            if pilihan == "1":
                cek_saldo(nomor_rekening)
            elif pilihan == "2":
                nomor_rekening_tujuan = input(bahasa["Masukkan_Nomor_Rekening_Tujuan"])
                jumlah = int(input(bahasa["Masukkan_Jumlah_Transfer"]))
                transfer(nomor_rekening, nomor_rekening_tujuan, jumlah)
            elif pilihan == "3":
                tarik_tunai(nomor_rekening)
            elif pilihan == "4":
                ganti_pin(nomor_rekening)
            elif pilihan == "5":
                riwayat(nomor_rekening)
            elif pilihan == "6":
                show_help()
            elif pilihan == "7":
                bayar_tagihan(nomor_rekening)
            elif pilihan == "8":
                print(bahasa["trmksh_menggunakan_atm"])
                break
            else:
                print("\033[31m" + bahasa["pilihan_valid"] + "\033[0m")

            if not transaksi_lagi():
                print(bahasa["trmksh_menggunakan_atm"])
                break
    else:
        print("\033[31m" + bahasa["login_gagal"] + "\033[0m")

while True:
    main()
    print("")  