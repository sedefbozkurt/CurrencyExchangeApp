# CurrencyExchangeApp

## Açıklama

CurrencyExchangeApp, ExchangeRate-API'yi kullanarak döviz kurlarını alıp dönüştüren bir Python uygulamasıdır. Kullanıcıların mevcut para birimlerini listelemesine, belirli bir tutarı bir para biriminden diğerine dönüştürmesine ve iki para birimi arasındaki döviz kurunu almasına olanak tanır.

## Özellikler

- Belirli bir temel para birimi için mevcut para birimlerini listeler
- Bir tutarı bir para biriminden diğerine dönüştürür
- İki para birimi arasındaki döviz kurunu alır

## Kurulum

1. Repoyu klonlayın:
  git clone https://github.com/sedefbozkurt/CurrencyExchangeApp.git

2. Proje dizinine gidin:
  cd currency-converter

3. Gerekli bağımlılıkları yükleyin:
  pip install requests python-dotenv

4. Proje dizininde bir `.env` dosyası oluşturun ve ExchangeRate-API anahtarınızı ekleyin:
  API_KEY=your_api_key_here

5. Kullanım
  python exchangeRate.py
