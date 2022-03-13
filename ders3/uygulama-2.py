#Kullanıcı adı ve şifre alınız.. kullanıcı adı olarak "admin" şifre olarak 123456 girilince "sisteme başarıyla giriş yaptınız" yazsın..
#yanlış girildikçe "kullanıcı adaı veya şifre  hatalı" yazıp
# tekrar kullanıcı adı şifre sorsun..

while True:
    Kullanıcıadı =input("Kullanıcı Adınız:")
    sifre = input("şifreniz:")
    if Kullanıcıadı=="admin" and sifre=="123456":
        break
    else:
        print("Kullanıcı adı ve şifre hatalı")

print("sisteme başarıyla giriş yaptınız..")



