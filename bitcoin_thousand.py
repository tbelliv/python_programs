import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch historical Bitcoin data from CoinGecko API (daily data)
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {"vs_currency": "usd", "days": "3650", "interval": "daily"}  # Fetch data for the last 10 years
response = requests.get(url, params=params)
data = response.json()

#timestamp and price extract
timestamps = [ts[0] // 1000 for ts in data["prices"]]
prices = [price[1] for price in data["prices"]]

#df creation
df = pd.DataFrame({"Timestamp": timestamps, "Price": prices})

# calc daily % change
df["PriceChange"] = df["Price"].pct_change()

# id prices close to perfect thousandth places
df["NearThousandth"] = ((df["Price"] % 1000) <= 100) | ((df["Price"] % 1000) >= 900)

#calc avg volatility
avg_volatility_near_thousandth = df[df["NearThousandth"]]["PriceChange"].abs().mean()
avg_volatility_not_near_thousandth = df[~df["NearThousandth"]]["PriceChange"].abs().mean()

print(f"Average volatility near perfect thousandth places: {avg_volatility_near_thousandth:.4f}")
print(f"Average volatility not near perfect thousandth places: {avg_volatility_not_near_thousandth:.4f}")

# plot
plt.figure(figsize=(10, 6))
plt.plot(df["Timestamp"], df["PriceChange"], label="Price Change")
plt.xlabel("Timestamp (daily)")
plt.ylabel("Percentage Change")
plt.title("Bitcoin Price Swings (Daily)")
plt.legend()
plt.show()
