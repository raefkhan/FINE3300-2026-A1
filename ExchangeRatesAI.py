"""
ExchangeRatesAI.py
FINE 3300 (Fall 2026) - Assignment #1, Part 2: Vibe Coding
Generated with Claude Opus 5.5 (Anthropic).

An exchange rate calculator that converts between USD and CAD using the
latest annual USD/CAD rate reported by the Bank of Canada.
"""

import csv
import glob
import os


class ExchangeRates:
    """Reads the Bank of Canada exchange rate file and converts USD <-> CAD."""

    # Column in the Bank of Canada file that holds the USD/CAD rate,
    # i.e. how many Canadian dollars one US dollar buys (CAD per 1 USD)
    USD_CAD_COLUMN = "FXAUSDCAD"

    def __init__(self, file_path):
        """Store the file path and read the latest USD/CAD rate from it."""
        self.file_path = file_path
        self.rate_date, self.usd_to_cad = self.read_latest_rate()

    def read_latest_rate(self):
        """Return the date and USD/CAD rate from the last row of the file."""
        # "utf-8-sig" removes the hidden byte-order mark at the very start of
        # the Bank of Canada file, which would otherwise corrupt the first
        # column name ("Date")
        with open(self.file_path, newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)  # each row becomes {column: value}
            # Keep only rows that actually have a USD/CAD value
            rows = [row for row in reader if row[self.USD_CAD_COLUMN]]

        # Rows are in chronological order, so the last row is the latest rate
        latest_row = rows[-1]
        return latest_row["Date"], float(latest_row[self.USD_CAD_COLUMN])

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency (USD or CAD) to the other."""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == "USD" and to_currency == "CAD":
            # The rate is CAD per 1 USD, so multiply to get CAD
            return amount * self.usd_to_cad
        if from_currency == "CAD" and to_currency == "USD":
            # Going the other way, divide by the rate to get USD
            return amount / self.usd_to_cad
        # Same currency in and out: nothing to convert
        return amount


def main():
    """Prompt the user, run the conversion and print the formatted result."""
    # Locate the CSV in the same folder as this script, so the program works
    # no matter which folder the VS Code terminal starts in. The pattern
    # matches both "BankOfCanadaExchangeRates.2026.csv" (the name in the
    # assignment) and "BankOfCanadaExchangeRate.2026.csv"
    script_folder = os.path.dirname(os.path.abspath(__file__))
    csv_file = glob.glob(os.path.join(script_folder, "BankOfCanadaExchangeRate*.csv"))[0]

    rates = ExchangeRates(csv_file)

    # Collect the three inputs (assumed valid, per the assignment); commas
    # are removed so an amount typed as 100,000 still reads as a number
    amount = float(input("Enter the amount: ").replace(",", ""))
    from_currency = input("Convert from (USD or CAD): ").upper()
    to_currency = input("Convert to (USD or CAD): ").upper()

    result = rates.convert(amount, from_currency, to_currency)

    # Format: dollar sign, comma separators, two decimals, currency code
    print(f"\nExchange rate used: 1 USD = {rates.usd_to_cad} CAD (Bank of Canada, {rates.rate_date})")
    print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")


# Runs automatically when the file is executed directly
if __name__ == "__main__":
    main()