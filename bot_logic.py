import datetime
import pytz
import time
import requests
import os

TWELVE_API_KEY = os.getenv("TWELVE_API_KEY")
WIB = pytz.timezone("Asia/Jakarta")

STOCK_GROUPS = {
    "Santai": ["AMD", "SPY", "AMZN", "VOO", "NVDA"],
    "Options": ["XOM", "CVX", "LMT", "RTX", "QQQ", "ARKK", "TSLA"]
}

def get_price(ticker):
    url = f"https://api.twelvedata.com/price?symbol={ticker}&apikey={TWELVE_API_KEY}"
    try:
        r = requests.get(url)
        data = r.json()
        return float(data["price"]) if "price" in data else "N/A"
    except:
        return "N/A"

def generate_santai_message():
    now = datetime.datetime.now(WIB).strftime("%d %B %Y")
    msg = f"📊 INFORMASI SAHAM HARI INI ({now})\n===================="
    for ticker in STOCK_GROUPS["Santai"]:
        price = get_price(ticker)
        msg += f"\n\n♦ {ticker}\n💰 {price}\n────────────"
    return msg

def generate_options_prices():
    now = datetime.datetime.now(WIB).strftime("%d %B %Y")
    msg = f"📢 SAHAM OPTIONS (Harga Saja) {now}\n====================="
    for ticker in STOCK_GROUPS["Options"]:
        price = get_price(ticker)
        msg += f"\n\n♦ {ticker}\n💰 {price}\n━━━━━━━━━━━━━━━"
    return msg

def get_news_only():
    return "📰 Pasar global stabil. Belum ada eskalasi geopolitik besar."
