from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackQueryHandler, ApplicationBuilder, MessageHandler, \
    filters, ContextTypes
from dotenv import load_dotenv
from typing import Union

import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN_ID")


async def message_monitor(update: Update, message: str, reply_markup: Union[
    InlineKeyboardMarkup, ReplyKeyboardMarkup, None] = None):
    if update.message:
        await update.message.reply_text(message, reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.answer()
        if isinstance(reply_markup, ReplyKeyboardMarkup):
            await update.callback_query.message.reply_text(message, reply_markup=reply_markup)
        else:
            await update.callback_query.message.edit_text(message, reply_markup=reply_markup)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Привет! Я учебный бот. Выбери команду ниже."
    keyboard = [["Меню", "Помощь"]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True)
    await message_monitor(update, message, reply_markup)


async def press_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Ты нажал кнопку!"
    await message_monitor(update, message)


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Это меню с онлайн кнопками. Выбери действие:"
    buttons = [
        [InlineKeyboardButton("Открыть сайт", url="https://www.python.org"),
         InlineKeyboardButton("Нажми меня!", callback_data="press_me")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message_monitor(update, message, reply_markup)


async def help_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "Я бот с кнопками. Мои команды: "
    buttons = [
        [InlineKeyboardButton("Запуск бота", callback_data="start"),
         InlineKeyboardButton("Меню", callback_data="menu")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message_monitor(update, message, reply_markup)


async def inline_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    callback_map = {
        "start": start,
        "press_me": press_me,
        "menu": menu,
    }
    if query.data in callback_map:
        await callback_map[query.data](update, context)
    else:
        await query.edit_message_text("Неизвестная команда.")


async def reply_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    buttons_map = {
        "Меню": menu,
        "Помощь": help_bot,
    }
    if text in buttons_map:
        await buttons_map[text](update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите кнопку.")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_bot))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_button_handler))
    app.add_handler(CallbackQueryHandler(inline_button_handler))
    print("Bot is polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
