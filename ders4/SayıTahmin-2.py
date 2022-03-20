import random
while True:
    seviye=input("Bir seviye seçiniz: kolay/orta/zor:")
    
    if seviye=="kolay":
        uret=random.randint(1,10)
        break
    if seviye=="orta":
        uret=random.randint(1,50)
        break
    if seviye=="zor":
        uret=random.randint(1,100)
        break
    else:
        print("Lütfen doğru seçim yapınız!")
while True:
    tahmin=int(input("Bir tahminde bulununuz:"))
    if tahmin<uret:
        print("Sayınızı büyültün")
    elif tahmin>uret:
        print("Sayınızı küçüültün")
    else:
        print("Tebrikler, bildiniz!")
        break
