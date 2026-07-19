# Mock Data Streamer for Photon
import random
import asyncio

stocks = {
    "AAPL": 190.00,
    "GOOG": 175.00,
    "TSLA": 310.00,
    "AMZN": 210.00,
    "MSFT": 420.00
}
def update_prices():
    for stock in stocks:
        change = random.uniform(-3, 3)
        stocks[stock] += change
        stocks[stock] = round(stocks[stock], 2)