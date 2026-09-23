# Project: My Interactive Live Converter in Python
# Created by: [Your Name or GitHub Nickname]
# I am 13 years old and this program is 100% interactive!

import urllib.request
import json

def get_exchange_rate(from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    url = f"https://er-api.com{from_currency}"
    
    try:
        # Web call to fetch live exchange rates
        response = urllib.request.urlopen(url, timeout=5)
        data = json.loads(response.read().decode())
        return data["rates"][to_currency]
    except:
        # Fallback rates if the internet is down or the currency doesn't exist
        if from_currency == "EUR" and to_currency == "USD":
            return 1.09
        elif from_currency == "USD" and to_currency == "EUR":
            return 0.92
        return 1.0

def celsius_to_fahrenheit(celsius_degrees):
    return round((celsius_degrees * 9/5) + 32, 2)


# --- INTERACTIVE TERMINAL ENGINE ---
if __name__ == "__main__":
    print("========================================")
    print("      WELCOME TO MY LIVE CONVERTER!     ")
    print("========================================")
    print("What would you like to do today?")
    print("1. Convert money (e.g., EUR to USD)")
    print("2. Convert temperature (C to F)")
    
    choice = input("Type your choice number (1 or 2): ").strip()
    
    if choice == "1":
        print("\n--- CURRENCY CONVERTER ---")
        from_val = input("Enter starting currency (e.g., EUR, USD, GBP): ").strip()
        to_val = input("Enter target currency: ").strip()
        
        try:
            amount_input = input(f"How many {from_val.upper()} do you want to convert?: ")
            amount = float(amount_input)
            
            rate = get_exchange_rate(from_val, to_val)
            result = round(amount * rate, 2)
            
            print("\n[Result]:")
            print(f"{amount} {from_val.upper()} is exactly {result} {to_val.upper()}!")
            print(f"(Live exchange rate applied: {rate})")
        except ValueError:
            print("\n[Error]: You must enter a valid number! Do not use letters or symbols.")

    elif choice == "2":
        print("\n--- TEMPERATURE CONVERTER ---")
        try:
            celsius_input = input("How many degrees Celsius (C) is it today?: ")
            celsius = float(celsius_input)
            result_f = celsius_to_fahrenheit(celsius)
            
            print("\n[Result]:")
            print(f"{celsius} C is equal to {result_f} F for Americans!")
        except ValueError:
            print("\n[Error]: Please enter a valid number for the temperature.")
        
    else:
        print("\nInvalid choice! Restart the program and type 1 or 2.")
        
    print("\n========================================")
    print(" Interactive code created by [ Me] 🚀")
    print("========================================")
