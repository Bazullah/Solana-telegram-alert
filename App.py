from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Solana Telegram Alert Bot is running!"
