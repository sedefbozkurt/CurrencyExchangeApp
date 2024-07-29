# CurrencyExchangeApp

## Açıklama

CurrencyExchangeApp, ExchangeRate-API'yi kullanarak döviz kurlarını alıp dönüştüren bir Python uygulamasıdır. Kullanıcıların mevcut para birimlerini listelemesine, belirli bir tutarı bir para biriminden diğerine dönüştürmesine ve iki para birimi arasındaki döviz kurunu almasına olanak tanır.

## Özellikler

- Belirli bir temel para birimi için mevcut para birimlerini listeler.
- Bir tutarı bir para biriminden diğerine dönüştürür.
- İki para birimi arasındaki döviz kurunu alır.

## Kurulum

1. Repoyu klonlayın:

    ```sh
    git clone https://github.com/sedefbozkurt/CurrencyExchangeApp.git
    ```

2. Proje dizinine gidin:

    ```sh
    cd CurrencyExchangeApp
    ```

3. Gerekli bağımlılıkları yükleyin:

    ```sh
    pip install requests python-dotenv
    ```

4. Proje dizininde bir `.env` dosyası oluşturun ve ExchangeRate-API anahtarınızı ekleyin:

    ```env
    API_KEY=your_api_key_here
    ```

## Kullanım

Uygulamayı çalıştırmak için:

```sh
python exchangeRate.py
