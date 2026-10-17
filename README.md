# FINE3300-2026-A1
A Python-based CAD/USD exchange rate calculator that reads annual exchange rate data from a file and converts between Canadian and US dollars using Python, Git, GitHub, and Visual Studio Code.

# Function of Each File

# 1. main.py
This is the main program that interacts with the user. It asks the user to enter the amount they want to convert, the original currency, and the target currency. It then calls the conversion function from `ExchangeRates.py` and displays the result.

Example: The user enters 100, USD, and CAD. The program passes these inputs to the `ExchangeRates` class to calculate the equivalent amount in Canadian dollars.

# 2. ExchangeRates.py
This file contains the `ExchangeRates` class, which handles reading the exchange rate from the dataset and performing the currency conversion. It supports conversions from USD to CAD and CAD to USD. It also checks whether the user has selected valid currencies.

Example: If the exchange rate is 1 USD = 1.37 CAD, converting 100 USD to CAD gives 137 CAD. Converting 137 CAD to USD gives 100 USD, using the same rate.

# 3. BankOfCanadaExchangeRate.2026.csv (Dataset)
This file contains exchange rate data from the Bank of Canada. The dataset provides the exchange rate used by the program to calculate the conversion between US dollars and Canadian dollars. The Python program reads the CSV file to retrieve the relevant rate rather than requiring the user to enter it manually.

Example: If the dataset contains an exchange rate of 1.37 CAD per USD, the program uses that value to convert US dollars into Canadian dollars. The actual conversion depends on the rate stored in the dataset.

# Example of Program Execution

Suppose the exchange rate in the dataset is 1 USD = 1.37 CAD.

Enter the amount you would like to convert: 100
Enter the currency you would like to convert from (USD or CAD): USD
Enter the currency you would like to convert to (USD or CAD): CAD
The converted amount is: 137.0

The program multiplies 100 USD by the exchange rate of 1.37 to produce 137 CAD.
