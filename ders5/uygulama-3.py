#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek
#sonucunda True ya da False gönderen fonksiyonun python kodu
#kullanıcıadı: admin,şifre:123456 olmalı


while True:
    Kullanıcıadı =input("Kullanıcı Adınız:")
    sifre = input("şifreniz:")
    if Kullanıcıadı=="admin" and sifre=="123456":
        break
    else:
        print("Kullanıcı adı ve şifre hatalı")

print("sisteme başrıyla giriş yaptınız......")
