#string
print("Universita Bina Sarana Informatika".lower())
print("Universitas Bina Sarana Informatika".upper())
print("I Love Programming In Python".split())
print("I Love Python".startswith("I"))
print("Saya Belajar Python".endswith("on"))
print("-".join(['I','Love','You']))
print("Belajar Java Di BSI".replace('Java','Python'))

#aritmatika
print("--------------------------------------------")
print("Operator Aritmatika")
nilai1= int(input("Masukan Nilai Pertama :"))
nilai2=int(input("Masukan Nilai Kedua :"))
penjumlahan=nilai1+nilai2
print(nilai1,"+",nilai2,"=",penjumlahan)
pengurangan=nilai1-nilai2
print(nilai1,"-",nilai2,"=",pengurangan)
perkalian=nilai1*nilai2
print(nilai1,"*",nilai2,"=",perkalian)
pembagian=nilai1/nilai2
print(nilai1,"/",nilai2,"=",pembagian)
pemangkatan=nilai1**nilai2
print(nilai1,"**",nilai2,"=",pemangkatan)
pembagian_bulat=nilai1//nilai2
print(nilai1,"//",nilai2,"=",pembagian_bulat)

#pembanding
Operator_Lebih_Besar=nilai1>nilai2
print(nilai1,">",nilai2,"adalah",Operator_Lebih_Besar)
Operator_Lebih_Kecil=nilai1<nilai2
print(nilai1,"<",nilai2,"adalah",Operator_Lebih_Kecil)
operator_sama_dengan=nilai1==nilai2
print(nilai1,"==",nilai2,"adalah",operator_sama_dengan)
operator_tidak_sama_dengan=nilai1!=nilai2
print(nilai1,"!=",nilai2,"adalah",operator_tidak_sama_dengan)

