import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")
KO_FI = "https://ko-fi.com/soberchatai"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Голосовой чат", callback_data="voice")]]
    await update.message.reply_text(
        "Привет! Я твой ИИ-друг.\nГовори голосом — я слушаю.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Голос принят! Отвечаю... ☕")
    keyboard = [[InlineKeyboardButton("$1 — Спасибо", url=KO_FI)]]
    await update.message.reply_text("Помогло? Скинь чашку кофе ☕", reply_markup=InlineKeyboardMarkup(keyboard))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VOICE | filters.TEXT, handle_voice))
app.run_polling()
