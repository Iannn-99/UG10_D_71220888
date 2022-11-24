nama= input("Masukkan nama pemain pertama: ")
nama= input("Masukkan nama pemain kedua: ")
nama= input("Masukkan nama pemain ketiga: ")
c1=int(input("Masukkan jumlah kartu pemain pertama: "))
c2=int(input("Masukkan jumlah kartu pemain kedua: "))
c3=int(input("Masukkan jumlah kartu pemain ketiga: "))
if (c):
    print("{} menang dengan jumlah kartu sebanyak {}" .format(nama,c1 or c2 or c3))
else:
    print()