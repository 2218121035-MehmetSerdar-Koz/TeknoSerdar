import unittest
from unittest.mock import patch
import io
import random

# Orijinal fonksiyon
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

# Test sınıfı
class TestTahminOyunu(unittest.TestCase):

    @patch('builtins.input', side_effect=[50, 30, 70, 90, 80, 60, 40])  # Girdi sırasıyla
    @patch('builtins.print')  # Print fonksiyonunu mock'la
    @patch('random.randint', return_value=70)  # Hedef sayıyı sabitle
    def test_tahmin_oyunu_basarili(self, mock_random, mock_print, mock_input):
        tahmin_oyunu()  # Fonksiyonu çalıştır

        # Beklenen çıktılar
        mock_print.assert_any_call("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
        mock_print.assert_any_call("Daha küçük bir sayı dene!")  # 50 -> 70'e göre küçük
        mock_print.assert_any_call("Daha büyük bir sayı dene!")  # 30 -> 70'e göre küçük
        mock_print.assert_any_call("Tebrikler! Doğru tahmin ettin 🎉")  # 70 ile doğru tahmin

    @patch('builtins.input', side_effect=[50, 30, 70, 90, 80, 60, 40])  # Girdi sırasıyla
    @patch('builtins.print')  # Print fonksiyonunu mock'la
    @patch('random.randint', return_value=10)  # Hedef sayıyı sabitle
    def test_tahmin_oyunu_basarisiz(self, mock_random, mock_print, mock_input):
        tahmin_oyunu()  # Fonksiyonu çalıştır

        # Beklenen çıktılar
        mock_print.assert_any_call("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
        mock_print.assert_any_call("Daha küçük bir sayı dene!")  # 50 -> 10'a göre büyük
        mock_print.assert_any_call("Daha küçük bir sayı dene!")  # 30 -> 10'a göre büyük
        mock_print.assert_any_call("Daha küçük bir sayı dene!")  # 70 -> 10'a göre büyük
        mock_print.assert_any_call("Daha küçük bir sayı dene!")  # 90 -> 10'a göre büyük
        mock_print.assert_any_call("Daha küçük bir sayı dene!")  # 80 -> 10'a göre büyük
        mock_print.assert_any_call("Daha küçük bir sayı dene!")  # 60 -> 10'a göre büyük
        mock_print.assert_any_call("Daha küçük bir sayı dene!")  # 40 -> 10'a göre büyük
        mock_print.assert_any_call("Üzgünüm, hakkın bitti. Tutulan sayı 10 idi.")

    @patch('builtins.input', side_effect=[
