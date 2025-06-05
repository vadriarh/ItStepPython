from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler, ApplicationBuilder, MessageHandler, \
    filters, ConversationHandler
from dotenv import load_dotenv

import os

from lessons.ItStep.lesson18.bd_tgbot import add_user, get_user

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN_ID")

async def start(update: Update, context: CallbackContext):
    user = update.effective_user
    add_user(user.username, user.id)
    await update.message.reply_text(f"Привет, {user.username}")

async def user(update: Update, context: CallbackContext):
    user = get_user(update.effective_user.id)
    await update.message.reply_text(
        f"Информация о пользователе:\n" + "\n".join(f"{key}: {value}" for key, value in user.items()))
    
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("user", user))
    print("Bot is polling...")
    app.run_polling()


if __name__ == "__main__":
    main()