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

    print(data)

def get_historical_ron_exchange_rate():
    pass

def save_exchange_rate_to_db():
    pass

def menu():
    get_latest_ron_exchange_rate()

if __name__ == "__main__":
    menu()