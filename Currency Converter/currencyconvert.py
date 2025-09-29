def currency_converter():
    rates = {
        'INR': 82.5,
        'EUR': 0.91,
        'GBP': 0.78
    }
    print("Currency Converter: USD to INR, EUR, GBP")
    
    try:
        usd_amount = float(input("Enter amount in USD: "))
        currency = input("Convert to (INR/EUR/GBP): ").upper()
        
        if currency in rates:
            converted_amount = usd_amount * rates[currency]
            print(f"{usd_amount} USD = {converted_amount:.2f} {currency}")
        else:
            print("Unsupported currency.")
    except ValueError:
        print("Invalid amount entered.")

if __name__ == "__main__":
    currency_converter()
