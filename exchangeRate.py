import os
import requests
from dotenv import load_dotenv # type: ignore

load_dotenv()

apiKey = os.getenv('API_KEY')

def getExchangeRates(apiKey, baseCurrency):
  url = f'https://v6.exchangerate-api.com/v6/{apiKey}/latest/{baseCurrency}'

  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    #print(data)
    return data.get('conversion_rates', {})
  except requests.exceptions.HTTPError as httpError:
    print(f"HTTP hatası oluştu: {httpError}")
  except requests.exceptions.RequestException as err:
    print(f"Hata: {err}")
  return {}

def getExchangeRate(apiKey, baseCurrency, targetCurrency):
  rates = getExchangeRates(apiKey, baseCurrency)
  return rates.get(targetCurrency.upper(), None)

def listAvaliableCurrencies(apiKey, baseCurrency):
  rates = getExchangeRates(apiKey, baseCurrency)
  if rates:
    print(f"{baseCurrency} için mevcut para birimleri: ")
    for cuurency in rates:
      print(cuurency)
  else:
    print("Kullanılabilir para birimi bulunamadı.")

def convertCurrency(apiKey, baseCurrency, targetCurrency, amount):
  exchangeRate = getExchangeRate(apiKey, baseCurrency, targetCurrency)
  if exchangeRate:
    convertedAmount = amount * exchangeRate
    print(f"{amount} {baseCurrency} = {convertedAmount:.2f}")
  else:
    print(f"Hata: {baseCurrency} ile {targetCurrency} arasında döviz kuru bulunamıyor")

def main():
  while True:
    print("\nDöviz Uygulamasına Hoşgeldiniz")
    print("1. Kullanılabilir Para Birimlerini Listele")
    print("2. Bir Para Birimini Farklı Bir Para Birimine Dönüştür")
    print("3. İki Para Biriminin Döviz Kurunu Al")
    print("4. Çıkış")
    choice = input("Seçiminiz: ")
    if choice == '1':
      baseCurrency = input("Temel para birimini girin (ör. USD): ").upper()
      listAvaliableCurrencies(apiKey, baseCurrency)
    elif choice == '2':
      baseCurrency = input("Temel para birimini girin (ör. USD): ").upper()
      targetCurrency = input("Hedef para birimini girin (ör. TRY): ").upper()
      while True:
        amountInput = input(f"Tutarı {baseCurrency} cinsinden girin: ")
        try:
          amount = float(amountInput)
          if amount < 0:
            print("Tutar negatif olamaz. Lütfen pozitif bir sayı girin.")
          else:
            break
        except ValueError:
          print("Geçersiz giriş! Lütfen sayısal bir değer girin.")

      convertCurrency(apiKey, baseCurrency, targetCurrency, amount)
    elif choice == '3':
      baseCurrency = input("Temel para birimini girin (ör. USD): ").upper()
      targetCurrency = input("Hedef para birimini girin (ör. TRY): ").upper()
      exchangeRate = getExchangeRate(apiKey, baseCurrency, targetCurrency)
      if exchangeRate:
        print(f"1 {baseCurrency} = {exchangeRate} {targetCurrency} ")
      else:
        print(f"Hata: {baseCurrency} ile {targetCurrency} arasında döviz kuru bulunamadı")
    elif choice == '4':
      print("Çıkış yapılıyor...")
      break
    else:
      print("Geçersiz seçenek. Lütfen tekrar deneyin")

if __name__ == "__main__":
    main()