import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Токен из переменной окружения
TOKEN = os.getenv("TOKEN")
KO_FI = "https://ko-fi.com/soberchatai"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Голосовой чат", url=KO_FI)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Я твой ИИ-друг. \nГовори голосом — я слушаю!",
        reply_markup=reply_markup
    )

# Обработка голосовых сообщений
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("$1 — Спасибо!", url=KO_FI)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Голос принят! Отвечаю...\n(Пока заглушка — скоро ИИ!)",
        reply_markup=reply_markup
    )

# Создание приложения
app = Application.builder().token(TOKEN).build()

# Регистрация хендлеров
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, handle_voice))

# Запуск бота ТОЛЬКО при прямом запуске
if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)
