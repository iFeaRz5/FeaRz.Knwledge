ulang=int(input("Masukan banyaknya data :"))
for i in range(ulang):
 print ("data Ke - " + str(i+1))
 print("===========Masukan data anda===========")
 nama=input("Masukan Nama kamu :")
 nim=input("Masukkan Nim anda : ")
 uts=int(input("Masukkan Nilai UTS anda :"))
 uas=int(input("Masukkan Nilai UAS : "))
 print("============== Hasil Tes ===============")
 print("Nama : %s" % (nama))
 print("NIM anda adalah %s" % (nim))
 print("nilai UTS anda %i " % (uts))
 print("nilai UAS anda %i" % (uas))
 avg= (uts+uas)/2
 print("Nilai Rata-rata anda adalah : %s" %(avg))
 if avg>70:
    print("Anda Lulus")
 else :
     print("Anda Tidak Lulus")
 print("=====================================\n")


