import requests
import sqlite3
from datetime import datetime

API_ENDPOINT = "https://v6.exchangerate-api.com/v6/"
API_KEY = "5798bdf5beabad95cb858948"

EXCHANGE_BASE = "RON"


def get_latest_ron_exchange_rate():
    url = f"{API_ENDPOINT}{API_KEY}/latest/{EXCHANGE_BASE}"

    response = requests.get(url)
    data = response.json()

    if data.get('result') == 'success':
        conversion_rates = data.get('conversion_rates', {})
        current_date = datetime.now().strftime('%Y-%m-%d')

        result_data = {
            'date': current_date,
            'conversion_rates': conversion_rates
        }

        return result_data
    else:
        print(f"Error: {data.get('error', {}).get('info')}")
        return None

def get_historical_ron_exchange_rate():
    pass

def save_exchange_rate_to_db():
    pass

def menu():
    result_data = get_latest_ron_exchange_rate()

    if result_data:
        date = result_data.get('date')
        conversion_rates = result_data.get('conversion_rates')

        print(f"Date: {date}")
        print("Conversion Rates:")
        for currency_code, rate in conversion_rates.items():
            print(f"{currency_code}: {rate}")

if __name__ == "__main__":
    menu()