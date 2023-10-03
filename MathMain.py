isim = input("Merhaba, isminiz nedir? ")
input("Merhaba " + isim + " oyunumuzda tuşladığın sayı 1'den sonsuza kadar çarpılmaya devam ediyor. Hazırsan başlayalım? (e/h) ")

print("Matematik Oyunu!")
print()
mult = int(input("Sayınızı tuşlayınız: "))
print()
count = 0
for i in range(1, 11):
    ans = int(input(str(i) + " X " + str(mult) + " = "))
    if ans == i*mult:
        print("Tebrikler!")
        count += 1
    else:
        print("Hayır! cevap ", i*mult,"!")
print()
print("------")
print()
print("Skorun ", "10/" ,count, )
