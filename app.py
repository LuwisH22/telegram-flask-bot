from flask import Flask, request
import requests
import os

from bot_logic import generate_santai_message, generate_options_prices, get_news_only

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Webhook endpoint
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/saham santai":
            msg = generate_santai_message()
            send_telegram(chat_id, msg)
        elif text == "/saham options":
            msg = generate_options_prices()
            send_telegram(chat_id, msg)
        elif text == "/news":
            msg = get_news_only()
            send_telegram(chat_id, msg)
        else:
            send_telegram(chat_id, "Command tidak dikenal.")

    return {"ok": True}

# Fungsi kirim pesan ke Telegram
def send_telegram(chat_id, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)

# Endpoint tes hidup
@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(debug=True)
