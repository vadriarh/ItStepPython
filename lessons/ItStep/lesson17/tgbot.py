from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler, ApplicationBuilder, MessageHandler, \
    filters, ConversationHandler
from dotenv import load_dotenv

import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN_ID")


async def start(update: Update, context: CallbackContext):
    name = update.effective_user.first_name
    await update.message.reply_text(f"Привет, {name}.", reply_markup=ReplyKeyboardRemove())


async def help(update: Update, context: CallbackContext):
    keybord = ReplyKeyboardMarkup([["/start", "/help"], ["/about"]], resize_keyboard=True)
    message = ("Список доступных команд:\n"
               "- /start — приветствие\n"
               "- /help — список команд\n"
               "- /about — кто я такой\n"
               "- /time — текущее время\n"
               "- /echo — повторяет текст\n"
               "- /reverse — переворачивает фразу\n"
               "- /status — загрузка системы")
    await update.message.reply_text(message, reply_markup=keybord)


async def about(update: Update, context: CallbackContext):
    message = "Я учебный Telegram-бот, созданный на Python с использованием async библиотеки."
    await update.message.reply_text(message)


async def menu(update: Update, context: CallbackContext):
    buttons = [
        [InlineKeyboardButton("Статус системы", callback_data="status"),
         InlineKeyboardButton("О боте", callback_data="about")],
        [InlineKeyboardButton("Сайт", url="https://t.me/@itstep_waw_2025_telegram_bot")],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(
        "Выберите действие: ", reply_markup=keyboard
    )


async def contacts(update: Update, context: CallbackContext):
    buttons = [
        [InlineKeyboardButton("Telegram", callback_data="telegram_url"),
         InlineKeyboardButton("GitHub", callback_data="git_url")]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(
        "Выберите действие: ", reply_markup=keyboard
    )

#update.message - это объект, который содержит информацию о сообщении, которое было отправлено в чат
#update.callback_query - это объект, который содержит информацию о нажатой кнопке CallbackQueryHandler
#update.message.text - это текст сообщения, которое было отправлено в чат вклюячая команды
#update.inline_query - это объект, который содержит информацию о нажатой кнопке в инлайн-клавиатуре

async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == 'status':
        await query.message.reply_text("Статус системы:\nCPU: 20%\nRAM: 30%")
    elif query.data == 'about':
        await query.message.reply_text("Этот бот создан для демонстрации возможностей Telegram API.")
    elif query.data == 'telegram_url':
        await query.message.reply_text(f"Вот мой Telegram: t.me/{query.from_user.username}")
    elif query.data == 'git_url':
        await query.message.reply_text("Вот мой GitHub: github.com/vadriarh")
    else:
        await query.message.reply_text("Неизвестная команда.")


NAME, AGE = range(2)


async def start_conv(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Как тебя зовут?")
    return NAME


async def get_name(update: Update, context: CallbackContext):
    pass


async def get_age(update: Update, context: CallbackContext):
    pass


async def cancel(update: Update, context: CallbackContext):
    pass


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start_conv)],
    states={
        NAME: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)
        ],
        AGE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)
        ]
    },
    fallbacs=[CommandHandler("cancel", cancel)]
)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("contacts", contacts))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, help))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(conv_handler)

    print("Bot is polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
