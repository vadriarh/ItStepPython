from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters, CallbackContext, \
    ApplicationBuilder, CallbackQueryHandler
from dotenv import load_dotenv

import os

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN_ID")
ADMIN_ID = os.getenv("ADMIN_ID")