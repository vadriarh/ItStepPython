from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters, CallbackContext, \
    ApplicationBuilder, CallbackQueryHandler
from dotenv import load_dotenv

import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN_ID")

NAME, AGE = range(2)


async def start_conv(update: Update, context: CallbackContext):
    context.user_data["user_info"] = {}
    await update.message.reply_text("Привет! Как тебя зовут?")
    return NAME


async def get_name(update: Update, context: CallbackContext):
    user_name = update.message.text
    context.user_data["user_info"]["name"]=user_name
    await update.message.reply_text(f"Круто, {user_name}! А сколько тебе лет?")
    return AGE


async def get_age(update: Update, context: CallbackContext):
    user_name = context.user_data["user_info"]["name"]
    user_age = update.message.text

    context.user_data["user_info"]["age"] = user_age
    await update.message.reply_text(f"Пользователь {user_name}, возраст {user_age}. Запомнил.")
    return ConversationHandler.END


async def cancel(update: Update, context: CallbackContext):
    context.user_data["user_info"]["name"] = "None"
    context.user_data["user_info"]["age"] = "None"
    await update.message.reply_text("Отмена диалога.")
    return ConversationHandler.END

async def info_user(update: Update, context: CallbackContext):

    if "user_info" in context.user_data.keys():
        user_info = context.user_data["user_info"]
        await update.message.reply_text(f"Пользователь {user_info["name"]}  возраст {user_info["age"]}")
    else:
        await update.message.reply_text(f"Пользователя не существует.")


async def info(update: Update, context: CallbackContext):
    user = update.message.from_user  # Получаем информацию о пользователе
    chat = update.message.chat  # Получаем информацию о чате

    info = {
        "Имя пользователя": user.first_name,
        "Фамилия пользователя": user.last_name,
        "ID пользователя": user.id,
        "Имя чата": chat.title if chat.title else "Нет",
        "ID чата": chat.id,
        "Тип чата": chat.type,
        "Дата создания": chat.created_at if hasattr(chat, 'created_at') else "Неизвестно"
    }
    await update.message.reply_text(
        f"Информация о пользователе:\n" + "\n".join(f"{key}: {value}" for key, value in info.items()))


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
    fallbacks=[CommandHandler("cancel", cancel)]
)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("info_user", info_user))
    app.add_handler(CommandHandler("info", info))

    print("Bot is polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
