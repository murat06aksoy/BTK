#dikdörtgenin  alanını ve çevresini hesaplayan 2 ayrı
# fonksiyon yazınız. Kullanıcıdan aldığınız değere göre
# alanı ve çevreyi ekrana yazdırınız


def çevre(kisa,uzun):
    return (kisa+uzun)*2
def alan(kisa,uzun):
    return kisa*uzun
kisa_kenar = int(input("Kisa kenar:"))
uzun_kenar = int(input("Uzun kenar:"))
print("Dikdörtgenin çevresi:",çevre(kisa_kenar,uzun_kenar))
print("Dikdörtgenin alanı:",alan(kisa_kenar,uzun_kenar))
