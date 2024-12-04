my_list= ['p','y','t','h','o','n','i','n','d','o']

#anggota list dari 3 s/d 5 (dari h s/d n)
print(my_list[3:6])

#anggota list dari 4 s/d  terakhir
print(my_list[4:])

#anggota list dari 0 s/d 4
print(my_list[:5])

#indeks dari belakang dari -1 s/d -4
print(my_list[-1:-5])

#misalkan  nilainya salah
ganjil=[1,3,4,7,9]

#ubah item ke 3(indeks ke2)
ganjil[2]=5
print(ganjil)

#mengubah sekali banyak
ganjil[2:5] = [11,13,15]
print(ganjil)

#menambahkan anggota list
ganjil=[1,3,5,7]
ganjil.append(9)
print(ganjil)
ganjil.extend([11,13,15])
print(ganjil)

#output 'y'
print(my_list.pop(1))
del my_list [2]

my_list.clear()
#output []
print (my_list)     