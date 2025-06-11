from flask import Flask, request
import os, requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Solana Telegram Alert Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    telegram_url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"
    chat_id = os.getenv('CHAT_ID')
    
    message = f"New transaction:\n{data}"
    
    requests.post(telegram_url, json={
        "chat_id": chat_id,
        "text": message
    })
    
    return {"status": "ok"}
