
from flask import Flask
from telegram.ext import Application, CommandHandler
import threading
import os

TOKEN = os.getenv("8488909748:AAFQySU8_ig54ia8YqR5F8hDGnqfOSZtwpM")

app = Flask(**name**)

@app.route("/")
def home():
return "Bot ishlayapti!"

async def start(update, context):
await update.message.reply_text("Salom! Bot ishlayapti.")

def run_bot():
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.run_polling()

if **name** == "**main**":
threading.Thread(target=run_bot, daemon=True).start()
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
