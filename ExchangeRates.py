import csv

class ExchangeRates:

    def __init__(self, filename): 
        
        self.rate = 0

        with open(filename, mode = 'r') as file:

            reader = csv.DictReader(file)
            for row in reader:
                if row['FXAUSDCAD'] != '':
                    self.rate = float(row['FXAUSDCAD'])

    def convert(self, amount, from_currency, to_currency):

        from_currency = from_currency.upper() # case sensitive, to make sure it sees upper case letters
        to_currency = to_currency.upper() # Samething for the to_currency

        if from_currency == 'USD' and to_currency == 'CAD': 
            return amount * self.rate # Since we are converting from USD to CAD, we multiply
        elif from_currency == 'CAD' and to_currency == 'USD':
            return amount / self.rate # Now we are converting from CAD to USD, so we divide.
        elif from_currency == to_currency:
            return amount # If the user by mistake uses the same currency for both.
        else:
            print("Invalid converstion. Please use either USD or CAD to convert to or from:) ")

