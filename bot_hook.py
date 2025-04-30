import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)
app = Flask(__name__)
dp = Dispatcher(bot, None, use_context=True)

def start(update, context):
    update.message.reply_text("Привет! Введите код доступа:")

def message_handler(update, context):
    text = update.message.text or ""
    if text.lower() == "abraforce2025":
        update.message.reply_text("Пароль верный! Теперь отправьте запрос на подбор аналогов.")
    else:
        update.message.reply_text(f"Вы написали:\n{text}\n(здесь будет поиск аналогов)")

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    upd = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(upd)
    return "OK"

if name == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
