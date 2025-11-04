import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print("1. Импорты прошли")

# Токен
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print("ОШИБКА: ТОКЕН НЕ НАЙДЕН!")
    exit(1)
else:
    print("2. Токен загружен")

KO_FI = "https://ko-fi.com/soberchatai"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("3. Команда /start вызвана")
    keyboard = [[InlineKeyboardButton("Голосовой чат", url=KO_FI)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Я твой ИИ-друг. \nГовори голосом — я слушаю!",
        reply_markup=reply_markup
    )

# Голос
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("4. Голосовое сообщение получено")
    keyboard = [[InlineKeyboardButton("$1 — Спасибо!", url=KO_FI)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Голос принят! Отвечаю...\n(Пока заглушка — скоро ИИ!)",
        reply_markup=reply_markup
    )

# Приложение
print("5. Создаём приложение...")
app = Application.builder().token(TOKEN).build()

print("6. Добавляем хендлеры...")
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, handle_voice))

# Запуск
if __name__ == "__main__":
    print("Bot is running... Поллинг запущен!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)
