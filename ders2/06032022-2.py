liste=[] # boş bir liste tanımlar
liste=["elma","armut",20] #artık listenin elemanları değişti!
sayilar=[15,9,8,25,6,4]
isimler=["olcay","ayşenur","murat","burak","yalçın"]
gunler=["Pazartesi","Salı","Çarşamba"]
print(gunler)
print("0. indeksdeki eleman:",gunler[0]) #ctrl+d satırı çoğaltır, ctrl+y satırı siler
print(gunler[1])
print(gunler[2])
gunler.append("Perşembe") #append: yeni elaman ekler
print(gunler)
print("eleman sayısı:",len(gunler)) #len: listenin eleman sayısını verir
gunler.pop() #hibirşey yazılmadığında listenini son elemanını çıkarır
gunler.pop(0) #0. indeksteki elamanı siler
print(gunler)
print(sayilar)
sayilar.sort() #varsayılan(default) olarak küçükten büyüğe doğru sıralar
print(sayilar)
sayilar.sort(reverse=True) #büyükten küçüğe doğru sıralar
print(sayilar)
isimler.sort()
print(isimler) #alfabeye göre sıralar
