import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        # Usa una URL genérica aquí, el endpoint podría variar dependiendo de la API que uses.
        self.url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/"

    def get_exchange_rate(self, from_currency, to_currency):
        # Construye la URL completa para la conversión
        full_url = self.url + from_currency
        response = requests.get(full_url)
        data = response.json()
        
        if response.status_code == 200:
            rates = data.get('conversion_rates', {})
            return rates.get(to_currency, None)
        else:
            error_message = data.get('error-type', 'Unknown error')
            print(f"Error: {error_message}")
            return None

        