nilai=int(input("Masukan Nilai Anda :"))
print('Nilai:',nilai)

if nilai>=90:
    print('A')
elif(nilai>=80)and(nilai<=90):
    print('B')
elif(nilai>=60)and(nilai<=80):
    print('C')
elif(nilai>=40)and(nilai<=60):
    print('D')
elif nilai<40:
    print('E')
else:
    print('Maaf,Format Tidak Sesuai')