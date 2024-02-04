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
        print(f"API Error: {data}")
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
        return None


def initialize_database():
    connection = sqlite3.connect("ron_currency_rates.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            currency_code TEXT,
            rate REAL
        )
    ''')

    connection.commit()
    connection.close()


def save_exchange_rate_to_db(result_data):
    try:
        connection = sqlite3.connect("ron_currency_rates.db")
        cursor = connection.cursor()

        date = result_data.get("date")
        conversion_rates = result_data.get("conversion_rates")

        for currency_code, rate in conversion_rates.items():
            cursor.execute('''
                SELECT * FROM exchange_rates
                WHERE date = ? AND currency_code = ?
            ''', (date, currency_code))

            existing_record = cursor.fetchone()

            if existing_record:
                cursor.execute('''
                    UPDATE exchange_rates
                    SET rate = ?
                    WHERE date = ? AND currency_code = ?
                ''', (rate, date, currency_code))
            else:
                cursor.execute('''
                    INSERT OR REPLACE INTO exchange_rates (date, currency_code, rate)
                    VALUES (?, ?, ?)
                ''', (date, currency_code, rate))

        connection.commit()
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
    finally:
        if connection:
            connection.close()


def menu():
    while True:
        print("\nMenu:\n1. Najnowszy kurs wymiany\n2. Kurs wymiany z danej daty\n3. Wyjście")
        choice = input("Wybierz opcję (1/2/3): ")

        if choice == "1":
            result_data = get_latest_ron_exchange_rate()
            if result_data:
                save_exchange_rate_to_db(result_data)

        elif choice == "2":
            date_str = input("Podaj datę w formacie YYYY-MM-DD (od 2018-01-01 do obecnej daty): ")

            try:
                input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                today_date = datetime.now().date()

                if input_date >= datetime(2018, 1, 1).date() and input_date <= today_date:
                    result_data = get_historical_ron_exchange_rate(date_str)
                    if result_data:
                        save_exchange_rate_to_db(result_data)
                else:
                    print("Błędna data. Proszę podać datę między 2018-01-01 a obecną datą.")

            except ValueError:
                print("Błędny format daty. Poprawny format to YYYY-MM-DD.")

        elif choice == "3":
            break

        else:
            print("Nieprawidłowy wybór. Wybierz opcję 1, 2 lub 3.")        


if __name__ == "__main__":
    initialize_database()
    menu()