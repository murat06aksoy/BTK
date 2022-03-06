#kullanıcıdan harf girmesinni isteyiniz e girerse erkek, k girerse kadın yazdırınız ekrana

cinsiyet=input("Bir harf giriniz E/K:")

if cinsiyet=="E" or cinsiyet=="e":
    print("Erkek")
elif cinsiyet=="K" or cinsiyet=="k": #2. veya daha fazla şart olursa elif kullanılır.
    print("Kadın")
else:
    print("Lütfen E veya K giriniz!")
print("HOŞÇAKALIN...")