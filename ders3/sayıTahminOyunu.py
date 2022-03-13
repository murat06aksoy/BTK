tuttugumsayi=7
while True:
    sayi=int(input("tahmininiz:"))
    if sayi<tuttugumsayi:
        print("Bilemedin,sayınızı büyütün!")
    elif sayi>tuttugumsayi:
        print("Bilemedin,sayınızı küçültün!")
    else:
        print("Tebrikler..Bildin..")
        break

