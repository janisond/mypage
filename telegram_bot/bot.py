import requests
import json
from datetime import datetime
from time import sleep

# Binance API endpoint for price ticker
BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/24hr?symbol="

# Telegram bot API endpoint
TELEGRAM_API_URL = "https://api.telegram.org/bot{}/sendMessage"

# Telegram bot token
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Chat ID of the Telegram channel where you want to send messages
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHANNEL_ID"

# Symbols for which you want to get price changes
SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]  # Add more symbols as needed

# Function to fetch price changes from Binance API
def get_price_changes(symbol):
    try:
        response = requests.get(BINANCE_API_URL + symbol)
        data = json.loads(response.text)
        price_change_percent = float(data['priceChangePercent'])
        return price_change_percent
    except Exception as e:
        print("Error fetching price changes:", e)
        return None

# Function to send message to Telegram
def send_telegram_message(message):
    try:
        url = TELEGRAM_API_URL.format(TELEGRAM_BOT_TOKEN)
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print("Failed to send message to Telegram:", response.text)
    except Exception as e:
        print("Error sending message to Telegram:", e)

# Main function
def main():
    while True:
        for symbol in SYMBOLS:
            price_change = get_price_changes(symbol)
            if price_change is not None:
                message = f"Price change for {symbol}: {price_change:.2f}%"
                send_telegram_message(message)
                print("Message sent to Telegram:", message)
        # Sleep for 60 seconds before fetching prices again
        sleep(60)

if __name__ == "__main__":
    main()

#test push to device