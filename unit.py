import unittest
from unittest.mock import patch
from tahmin_oyunu import tahmin_oyunu

class TestTahminOyunu(unittest.TestCase):
    @patch('tahmin_oyunu.random.randint', return_value=50)
    def test_dogru_tahmin(self, mock_randint):
        inputs = iter(["50"])
        result = tahmin_oyunu(lambda _: next(inputs))
        self.assertTrue(result)  # Doğru tahmin sonucu True olmalı

    @patch('tahmin_oyunu.random.randint', return_value=50)
    def test_yanlis_tahmin(self, mock_randint):
        inputs = iter(["30", "40", "45", "47", "48", "49", "51"])
        result = tahmin_oyunu(lambda _: next(inputs))
        self.assertFalse(result)  # Yanlış tahmin sonucu False olmalı

    @patch('tahmin_oyunu.random.randint', return_value=50)
    def test_gecersiz_giris(self, mock_randint):
        inputs = iter(["abc", "50"])
        with patch('builtins.print') as mock_print:
            result = tahmin_oyunu(lambda _: next(inputs))
            self.assertTrue(result)  # Doğru tahmin sonucu True olmalı
            mock_print.assert_any_call("Lütfen bir sayı gir!")  # Geçersiz giriş uyarısı kontrol edilir

if __name__ == "__main__":
    unittest.main()
