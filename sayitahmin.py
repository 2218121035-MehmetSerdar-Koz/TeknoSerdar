import random

def tahmin_oyunu():
    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
    hedef = random.randint(1, 100)
    tahmin_hakki = 7

    while tahmin_hakki > 0:
        try:
            tahmin = int(input(f"Kalan hakkın {tahmin_hakki}. Tahminin: "))
        except ValueError:
            print("Lütfen bir sayı gir!")
            continue

        if tahmin < hedef:
            print("Daha büyük bir sayı dene!")
        elif tahmin > hedef:
            print("Daha küçük bir sayı dene!")
        else:
            print("Tebrikler! Doğru tahmin ettin 🎉")
            return

        tahmin_hakki -= 1

    print(f"Üzgünüm, hakkın bitti. Tutulan sayı {hedef} idi.")

tahmin_oyunu()
