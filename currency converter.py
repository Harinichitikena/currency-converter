import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Error: Unable to fetch data for {from_currency.upper()}"

    data = response.json()
    rates = data.get("rates")

    if to_currency.upper() not in rates:
        return f"Error: Currency '{to_currency.upper()}' not supported."

    converted_amount = amount * rates[to_currency.upper()]
    return f"{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}"

# Example usage
amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ")
to_currency = input("To currency (e.g., INR): ")

result = convert_currency(amount, from_currency, to_currency)
print(result)
