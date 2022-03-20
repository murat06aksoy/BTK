#Kullanıcıdan bir sayı girmesini isteyen,
# sayı girmediğinde tekrar sayı girmesini isteyen,
# sayı girdiğinde de ekrana sayının karesini yazdıran program yapınız.


while True:
    try:
        sayi=int(input("Bir sayı giriniz:"))
        break
    except ValueError:
        print("Sadece sayı kabul etmekteyim!")
print("Karesi:",sayi**2)


