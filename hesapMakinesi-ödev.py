print("""HESAP MAKİNESİ""")
sayi1 = int(input("Birinci sayıyı giriniz:"))
islem = input("Bir İşlem Seçiniz: (+, -, *, /): ")

sayi2 = int(input("İkinci sayıyı giriniz:"))

if islem == "+":
    print(sayi1, "+", sayi2,"=", sayi1 + sayi2)
elif islem == "-":
    print(sayi1, "-", sayi2, "=", sayi1 + sayi2)
elif islem == "*":
    print(sayi1, "*", sayi2, "=", sayi1 + sayi2)
elif islem == "/":
    print(sayi1, "/", sayi2, "=", sayi1 + sayi2)
else:
    print("Programımızda böyle bir işlem bulunmamaktadır!!!", "(+, -, *, /)", "Lütfen bunlardan birini seçiniz" )