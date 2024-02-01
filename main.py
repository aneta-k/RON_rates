import requests
import sqlite3
from datetime import datetime

API_ENDPOINT = "https://api.exchangeratesapi.io/v1/"
API_KEY = "09fac5d2507b00fbecdf90473623a7d6"

EXCHANGE_BASE = "RON"
CURRENCY_SYMBOLS = "EUR,USD,CHF,GBP,BGN,RUB,ZAR,BRL,CNY,INR,MXN,NZD,RSD,UAH,TRY,AUD,CAD,CZK,DKK,EGP,MDL,NOK,PLN,SEK,AED,THB"

rates_params = {
    "access_key": API_KEY,
    "base": EXCHANGE_BASE,
    "symbols": CURRENCY_SYMBOLS
}

def get_latest_ron_exchange_rate():
    pass

def get_historical_ron_exchange_rate():
    pass

def save_exchange_rate_to_db():
    pass

def menu():
    pass

if __name__ == "__main__":
    menu()