import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 1. Берём токен из секретов Replit (Environment Secret)
TOKEN = os.getenv("BOT_TOKEN")

# 2. Обработчик команды /start
def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Введите код доступа:")

# 3. Обработка любого текстового сообщения (после входа)
#    Здесь позже будет ваша логика поиска по каталогу и построения таблицы
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    # TODO: заменить заглушку на реальный поиск аналогов
    if text.lower() == "abraforce2025":
        update.message.reply_text("Пароль верный! Теперь отправьте запрос на подбор аналогов.")
    else:
        update.message.reply_text(f"Вы написали:\n{text}\n(здесь будет ваш поиск аналогов)")

def main():
    # 4. Создаём Updater и Dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # 5. Регистрируем обработчики
    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    # 6. Запускаем опрос Telegram (polling)
    print("Bot is starting polling...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()