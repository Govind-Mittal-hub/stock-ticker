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


# Updates prices with small random changes
def update_prices():
    for stock in stocks:
        change = random.uniform(-3, 3)
        stocks[stock] += change
        stocks[stock] = round(stocks[stock], 2)


async def generate_stock_data():
    while True:
        update_prices()
        for ticker, price in stocks.items():
         print(f"{ticker}: ₹{price}")
        await asyncio.sleep(1)
        if __name__ == "__main__":
            asyncio.run(generate_stock_data())
            def get_stock_data():
             data = []

    for ticker, price in stocks.items():
        data.append({
            "ticker": ticker,
            "price": price
        })

    return data