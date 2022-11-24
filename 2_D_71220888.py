nama= input("Masukkan nama pemain pertama: ")
nama= input("Masukkan nama pemain kedua: ")
nama= input("Masukkan nama pemain ketiga: ")
c1=int(input("Masukkan jumlah kartu pemain pertama: "))
c2=int(input("Masukkan jumlah kartu pemain kedua: "))
c3=int(input("Masukkan jumlah kartu pemain ketiga: "))
if (c2<=21):
    print("{} menang dengan jumlah kartu sebanyak {}" .format(nama,c2))
else:
    print("Jumlah kartu yang dimiliki melebihi batas")