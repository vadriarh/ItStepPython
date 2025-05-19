from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ApplicationBuilder
from dotenv import load_dotenv
from datetime import datetime

import os
import psutil
import platform

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN_ID")


def logging(update: Update):
    print(f"{update.effective_user.username}: {update.message.text}")


async def start(update: Update, context: CallbackContext):
    logging(update)
    name = update.effective_user.first_name
    await update.message.reply_text(f"Привет, {name}.")


async def about(update: Update, context: CallbackContext):
    logging(update)
    message = "Я учебный Telegram-бот, созданный на Python с использованием async библиотеки."
    await update.message.reply_text(message)

async def time(update: Update, context: CallbackContext):
    logging(update)
    now = datetime.now().strftime("%H:%M:%S %d.%m.%Y")
    await update.message.reply_text(f"Текущее время по Варшаве: {now}")


async def echo(update: Update, context: CallbackContext):
    logging(update)
    message = update.message.text[6::1]
    if not message:
        await update.message.reply_text("(Allert)Звук неслышного эха.")
    else:
        await update.message.reply_text(message)



async def reverse(update: Update, context: CallbackContext):
    logging(update)
    message = update.message.text[9::1]
    if not message:
        await update.message.reply_text("(Allert)Не могу инвертировать пустую строку.")
    else:
        await update.message.reply_text(message[::-1])


async def status(update: Update, context: CallbackContext):
    logging(update)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    system = platform.system()
    message = (f"Текущее время: {current_time}\n"
               "\t\tСостояние системы\n"
               f"CPU: {cpu}%\n"
               f"RAM usage: {ram}%\n"
               f"DISK usage: {disk}%\n"
               f"System info: {system} system")
    await update.message.reply_text(message)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("time", time))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("reverse", reverse))
    app.add_handler(CommandHandler("status", status))

    print("Bot is polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
