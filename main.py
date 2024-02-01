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

    if data.get("result") == "success":
        conversion_rates = data.get("conversion_rates", {})
        current_date = datetime.now().strftime("%Y-%m-%d")

        result_data = {
            "date": current_date,
            "conversion_rates": conversion_rates
        }

        return result_data
    else:
        print(f"Error: {data.get('error', {}).get('info')}")
        return None

def get_historical_ron_exchange_rate(date_str):
    year, month, day = map(int, date_str.split("-"))

    url = f"{API_ENDPOINT}{API_KEY}/history/{EXCHANGE_BASE}/{year}/{month}/{day}"

    response = requests.get(url)
    data = response.json()

    if data.get("result") == "success":
        conversion_rates = data.get("conversion_rates", {})

        result_data = {
            "date": date_str,
            "conversion_rates": conversion_rates
        }

        return result_data
    else:
        print(f"API Error: {data}")
        print(f"Error: {data.get('error', {}).get('info')}")
        return None

def save_exchange_rate_to_db():
    pass

def menu():
    while True:
        print("\nMenu:\n1. Najnowszy kurs wymiany\n2. Kurs wymiany z danej daty\n3. Wyjście")
        choice = input("Wybierz opcję (1/2/3): ")

        if choice == "1":
            result_data = get_latest_ron_exchange_rate()
            if result_data:
                date = result_data.get("date")
                conversion_rates = result_data.get("conversion_rates")

                print(f"Data: {date}")
                print("Conversion Rates:")
                for currency_code, rate in conversion_rates.items():
                    print(f"{currency_code}: {rate}")

        elif choice == "2":
            date_str = input("Podaj datę w formacie YYYY-MM-DD (od 2018-01-01 do obecnej daty): ")

            try:
                input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                today_date = datetime.now().date()

                if input_date >= datetime(2018, 1, 1).date() and input_date <= today_date:
                    result_data = get_historical_ron_exchange_rate(date_str)
                    if result_data:
                        conversion_rates = result_data.get("conversion_rates")

                        print(f"Data: {date_str}")
                        print("Conversion Rates:")
                        for currency_code, rate in conversion_rates.items():
                            print(f"{currency_code}: {rate}")

                else:
                    print("Błędna data. Proszę podać datę między 2018-01-01 a obecną datą.")

            except ValueError:
                print("Błędny format daty. Poprawny format to YYYY-MM-DD.")

        elif choice == "3":
            break

        else:
            print("Nieprawidłowy wybór. Wybierz opcję 1, 2 lub 3.")        


if __name__ == "__main__":
    menu()