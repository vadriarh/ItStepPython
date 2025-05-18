from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ApplicationBuilder
from dotenv import load_dotenv
from datetime import datetime

import psutil
import platform
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN_ID")


async def start(update: Update, context: CallbackContext):
    if update.message.chat_id == 1649361940:
        await update.message.reply_text("Hello, Admin.")
    else:
        await update.message.reply_text("Hello, User.")


async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("/start - \"Hello\"\n"
                                    "/help - show you all commands\n")


async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text("Y")


async def status(update: Update, context: CallbackContext):
    if update.message.chat_id == 1649361940:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        system = platform.system()
        message = (f"Current time: {current_time}\n"
                   "\tSystem status\n"
                   f"CPU usage: {cpu}\n"
                   f"RAM usage: {ram}\n"
                   f"DISK usage: {disk}\n"
                   f"System info: {system}")
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("You do not have administrator privileges")




def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("status", status))

    print("bot is polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
