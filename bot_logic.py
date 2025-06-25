import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "7353553539:AAFl4gLI9AdEThliRVJ1tfUs9lfMeUOOtF4")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_message(chat_id, text):
    data = {"chat_id": chat_id, "text": text}
    requests.post(API_URL, data=data)

def handle_command(chat_id, text):
    if text == "/saham_santai":
        message = "📢 Saham Santai: AMD, SPY, AMZN, VOO, NVDA\n(harga akan ditampilkan di versi full)"
        send_message(chat_id, message)

    elif text == "/saham_options":
        message = "📢 Saham Options: XOM, CVX, LMT, dst\n(harga saja tanpa analisa)"
        send_message(chat_id, message)

    elif text == "/news":
        message = "🌐 Berita global terbaru akan tampil di sini."
        send_message(chat_id, message)

    else:
        send_message(chat_id, "Perintah tidak dikenali. Gunakan: /saham_santai /saham_options /news")