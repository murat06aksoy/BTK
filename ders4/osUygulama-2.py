import os
print("1- Klasör Oluştur")
print("2- Klasör sil")
secim=input("Seçiminiz:")
if  secim=="1":
    ad=input("Oluşturmak istediğiniz klasörün adı giriniz:")
    for i in range(1,11):
        os.mkdir(ad+str(i))
elif secim=="2":
    ad=input("Silmek istediğiniz klasörün adı giriniz:")
    for i in range(1,11):
        os.rmdir(ad+str(i))





