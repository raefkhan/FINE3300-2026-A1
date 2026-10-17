from ExchangeRates import ExchangeRates


def main():

    converter = ExchangeRates('BankOfCanadaExchangeRate.2026.csv')

    amount = float(input('Enter the amount you would like to convert: '))

    from_currency = input('Enter the currency you would like to convert from (USD or CAD): ')
    to_currency = input('Enter the currency you would like to convert to (USD or CAD): ')

    final_amount = converter.convert(amount, from_currency, to_currency)
    print(f'The converted amount is: {final_amount}')


main()