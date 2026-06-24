from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot ishlayapti!"

def bot_loop():
    while True:
        print("Bot ishlayapti...")
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=bot_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
