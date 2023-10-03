from random import randint

tahmin = randint(1, 50)
sayac = 0
dogruTahminMi = False
while (dogruTahminMi is False):
    sayac += 1
    girilenSayi = int(input("1 ile 50 arasında bir sayı giriniz."+
                            "(Çıkmak için 0(sıfır) ) :"))
    if(girilenSayi == 0):
        print("Oyundan Çıktınız.")
        break
    elif girilenSayi < tahmin:
        print("Düşük sayı girişi yaptınız. Daha yüksek bir sayı giriniz.")
        continue
    elif girilenSayi > tahmin:
        print("Yüksek bir sayı girişi yaptınız. Daha düşük bir sayı giriniz.")
        continue
    else:
        dogruTahminMi=True
        print("Doğru Tahmin. Rastgele tahmin edilen sayı {0}!".format(tahmin))
        print("Tahmin sayınız {0}".format(sayac))
