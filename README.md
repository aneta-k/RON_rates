## Program Wymiany Walut

Ten program napisany w Pythonie umożliwia pobieranie i aktualizowanie bieżących oraz archiwalnych kursów wymiany dla rumuńskiego leja (RON). Dane źródłowe pochodzą z API ExchangeRate.

### Funkcje

- **Najnowszy Kurs Wymiany:** Pobieranie najnowszego kursu wymiany dla rumuńskiego leja.
- **Kurs Wymiany Historyczny:** Pobieranie kursów wymiany dla określonej daty (od 2018-01-01 do teraz).
- **Przechowywanie Danych w Bazie Danych:** Zapisywanie i aktualizowanie danych o kursach wymiany w bazie danych SQLite.
- **Przyjazne dla Użytkownika Menu:** Interakcja z programem za pomocą prostego menu w konsoli.

### Wymagania

- Python 3.x
- Wymagane pakiety Pythona: `requests`, `sqlite3`
```bash
pip install requests sqlite3
```

### Użycie

1. Uruchom program:

```bash
python main.py
```

2. Postępuj zgodnie z menu ekranowym, aby wybrać żądaną operację:

- **Opcja 1: Pobierz najnowszy kurs wymiany.**
- **Opcja 2: Pobierz historyczne kursy wymiany dla określonej daty.**
- **Opcja 3: Zamknij program.**

### Baza Danych

- Program wykorzystuje SQLite do lokalnego przechowywania danych w bazie danych.
- Baza danych (ron_currency_rates.db) jest automatycznie tworzona i inicjowana przy uruchamianiu programu.

### Struktura Tabeli

```sql
CREATE TABLE IF NOT EXISTS exchange_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    currency_code TEXT,
    rate REAL
);
```

### Obsługa Błędów

- Program obejmuje obsługiwanie błędów dla nieprawidłowych wejść użytkownika i błędów API.
- Szczegółowe komunikaty o błędach są dostarczane, aby prowadzić użytkownika.