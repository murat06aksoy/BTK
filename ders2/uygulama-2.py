#kullanıcıdan 5 tane sayı iteyerek en büyük sayıyı listeye atayarak bulunuz!
sayilar=[]
sayi1=int(input("1. sayiyi giriniz:"))
sayi2=int(input("2. sayiyi giriniz:"))
sayi3=int(input("3. sayiyi giriniz:"))
sayi4=int(input("4. sayiyi giriniz:"))
sayi5=int(input("5. sayiyi giriniz:"))
sayilar=[]
sayilar.append(sayi1)
sayilar.append(sayi2)
sayilar.append(sayi3)
sayilar.append(sayi4)
sayilar.append(sayi5)
sayilar.sort()
print("girdiğiniz sayılardan en büyüğü:",sayilar[4])
