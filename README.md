## Currency Exchange Rate Updater

This Python program enables fetching and updating current and historical exchange rates for the Romanian Leu (RON). The data source is the ExchangeRate-API.

### Features

- **Latest Exchange Rate:** Fetching the most recent exchange rate for the Romanian Leu.
- **Historical Exchange Rate:** Retrieving exchange rates for a specified date (from 2018-01-01 to now).
- **Data Storage in the Database:** Saving and updating exchange rate data in an SQLite database.
- **User Menu:** Interacting with the program using a simple console menu.

### Requirements

- Python 3.x
- Required Python packages: `requests`, `sqlite3`

### Installation

1. Clone the repository:

```bash
git clone https://github.com/aneta-k/RON_rates.git
cd RON_rates
```

2. Install the required dependencies:

```bash
pip install requests
```

### Usage

1. Run the program:

```bash
python main.py
```

2. Follow the on-screen menu to choose options:

- **Option 1: Fetch and save the latest exchange rate.**
- **Option 2: Enter a specific date to fetch and save historical exchange rates.**
- **Option 3: Exit the program.**

### Database

- The program uses SQLite to store exchange rate data.
- The database file is named ron_currency_rates.db, and a table named exchange_rates is created to store the data when the program is first ran.

### Notes

- Make sure to replace the API_KEY variable with your valid ExchangeRate-API key.
- The program fetches data from [ExchangeRate-API](https://www.exchangerate-api.com/).
- Historical data is available from January 1, 2018, to the current date.