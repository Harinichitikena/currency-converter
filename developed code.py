import requests
from datetime import datetime

# File to store conversion history
HISTORY_FILE = "conversion_history.txt"

def save_history(entry):
    """Save each conversion result into a text file."""
    with open(HISTORY_FILE, "a") as file:
        file.write(entry + "\n")

def convert_currency(amount, from_currency, to_currency):
    """
    Convert amount from one currency to another using live exchange rates.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"

    try:
        # Get data from API
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request failed

        data = response.json()
        rates = data.get("rates", {})

        # Check if the target currency exists
        if to_currency.upper() not in rates:
            return f"❌ Error: Currency '{to_currency.upper()}' not supported."

        # Perform conversion
        converted_amount = amount * rates[to_currency.upper()]

        # Prepare result message
        result = f"✅ {amount:.2f} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}"

        # Save result to history with date & time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_history(f"[{timestamp}] {result}")

        return result

    except requests.exceptions.RequestException:
        return "❌ Network error! Please check your internet connection."

    except Exception as e:
        return f"❌ Unexpected error: {e}"

# ---------------- MAIN PROGRAM ----------------
print("💱 Welcome to Currency Converter (Live Rates)")
print("Type 'exit' anytime to quit.\n")

while True:
    try:
        # Get amount input
        amount_input = input("Enter amount: ").strip()
        if amount_input.lower() == "exit":
            print("\n📜 Conversion history saved in 'conversion_history.txt'. Goodbye!")
            break

        amount = float(amount_input)

        # Get base currency
        from_curr = input("From currency (e.g., USD): ").strip()
        if from_curr.lower() == "exit":
            break

        # Get target currency
        to_curr = input("To currency (e.g., INR): ").strip()
        if to_curr.lower() == "exit":
            break

        # Perform conversion
        result = convert_currency(amount, from_curr, to_curr)
        print(result + "\n")

    except ValueError:
        print("❌ Please enter a valid number for the amount.\n")
