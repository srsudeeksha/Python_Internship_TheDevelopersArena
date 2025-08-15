# week8_stock_tracker.py

import requests
import json

def get_stock_price(symbol):
    """Fetch stock price from a free API."""
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=YOUR_API_KEY"
    try:
        response = requests.get(url)
        data = response.json()
        if "c" in data:
            return data["c"]
        else:
            print("❌ Error fetching stock data.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ API Error: {e}")
        return None

def main():
    print("📈 Stock Price Tracker")
    symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    price = get_stock_price(symbol)
    if price:
        print(f"💵 Current price of {symbol}: ${price}")

if __name__ == "__main__":
    main()
