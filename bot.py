import os
+import sys
+import logging
 from telegram import Update
 from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

+# Включим логирование в stdout, чтобы всё сразу шло в лог Railway
+logging.basicConfig(
+    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
+    level=logging.INFO
+)
+logger = logging.getLogger(__name__)

 # 1. Берём токен из секретов Replit / Railway (Environment Secret)
 TOKEN = os.getenv("BOT_TOKEN")
+if not TOKEN:
+    # если токен не установлен — сразу выйдем и напишем это в лог
+    logger.error("BOT_TOKEN не найден в окружении! Задать переменную BOT_TOKEN нужно в настройках Railway.")
+    sys.exit(1)
+else:
+    logger.info("BOT_TOKEN успешно загружен.")

 def start_handler(update: Update, context: CallbackContext):
     update.message.reply_text("Привет! Введите код доступа:")

 def message_handler(update: Update, context: CallbackContext):
     text = update.message.text
     if text.lower() == "abraforce2025":
         update.message.reply_text("Пароль верный! Теперь отправьте запрос на подбор аналогов.")
     else:
         update.message.reply_text(f"Вы написали:\n{text}\n(здесь будет ваш поиск аналогов)")

 def main():
-    updater = Updater(TOKEN, use_context=True)
+    # проверяем, что Updater удаётся инициализировать
+    try:
+        updater = Updater(TOKEN, use_context=True)
+    except Exception as e:
+        logger.exception("Не удалось создать Updater:")
+        sys.exit(1)
     dp = updater.dispatcher

     dp.add_handler(CommandHandler("start", start_handler))
     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

     print("Bot is starting polling...")
     updater.start_polling()
     updater.idle()

 if name == "__main__":
     main()