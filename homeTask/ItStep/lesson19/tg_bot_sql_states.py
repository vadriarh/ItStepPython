import sqlite3
import time

import homeTask.ItStep.lesson19.sql_components as sql_components
import os

from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes, filters, MessageHandler, \
    CallbackQueryHandler, ConversationHandler

from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN_ID")


# команды бота

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["Добавить", "Баланс"], ["История", "Помощь"]]
    reply_markup = ReplyKeyboardMarkup(
        reply_keyboard,
        resize_keyboard=True,
        one_time_keyboard=False)
    await update.message.reply_text("Приветствую в кошельке", reply_markup=reply_markup)


async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    result = sql_components.get_balance(user_id)
    if result:
        await update.message.reply_text(
            f"Ваш баланс: {result["balance"]} (Доход: {result["income"]}, Расход: {result["expense"]})")
    else:
        await update.message.reply_text("Ошибка получения баланса из базы данных.")


async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    rows = sql_components.get_history(user_id)
    if rows is None:
        await update.message.reply_text("Ошибка получения истории из базы данных.")
    elif rows:
        result = "Последние 5 транзакций:\n"
        for row in rows:
            result += f"{row[3]} - {row[0]}: {row[1]} (Описание: {row[2]})\n"
        await update.message.reply_text(result)
    else:
        await update.message.reply_text("Нет сохранённых транзакций.")


async def help_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = (f"Данный бот - личный кошелек для учета доходов и расходов.\n\n"
                    f"Доступные команды:\n"
                    f"       /add     - добавить новую транзакцию\n"
                    f"       /balance - показать текущий баланс\n"
                    f"       /history - показать последние операции\n"
                    f"       /help    - показать эту справку\n"
                    f"       /cancel  - отменить текущую операцию\n\n"
                    f"Или используйте кнопки:")
    await update.message.reply_text(help_message)


async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    result = sql_components.get_summary_history(user_id)
    if result:
        await update.message.reply_text(
            f"Общий размер транзакций по катешориям:\n"
            f" \t\t(Доход: {result["income"]}\n"
            f" \t\tРасход: {result["expense"]})")
    else:
        await update.message.reply_text("Ошибка получения баланса из базы данных.")

# обработчик состояний

TYPE, AMOUNT, DESCRIPTION = range(3)


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    inline_keyboard = [
        [InlineKeyboardButton("Доход", callback_data="income"),
         InlineKeyboardButton("Расход", callback_data="expense")],
        [InlineKeyboardButton("Отменить", callback_data="cancel")]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await update.message.reply_text("Выберите тип операции", reply_markup=reply_markup)
    return TYPE


async def choose_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if update.callback_query.data == "cancel":
        await query.edit_message_text("Операция отменена.")
        return ConversationHandler.END
    context.user_data["type"] = query.data  # Сохраняем тип операции {"type": "income" или "expense"}
    await query.edit_message_text("Какая сумма операции?")
    return AMOUNT


async def set_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(update.message.text)
        context.user_data["amount"] = amount
        await update.message.reply_text("Введите описание операции:")
        return DESCRIPTION
    except ValueError:
        await update.message.reply_text("Пожалуйста, введите корректную сумму.")
        return AMOUNT


async def set_description(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    type_transaction = "доход" if context.user_data["type"] == "income" else "расход"
    amount = context.user_data["amount"]
    description = update.message.text
    result = sql_components.add_transaction(user_id, type_transaction, amount, description)
    if result:
        await update.message.reply_text(
            f"Операция добавлена:\nТип: {type_transaction}\nСумма: {amount}\nОписание: {description}")
    else:
        await update.message.reply_text("Ошибка обращения к базе данных для записи транзакции.")
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Операция отменена.")
    return ConversationHandler.END


conv_handler_add = ConversationHandler(
    entry_points=[
        CommandHandler("add", add),
        MessageHandler(filters.TEXT & filters.Regex("^Добавить$"), add)
    ],
    states={
        TYPE: [
            CallbackQueryHandler(choose_type)
        ],
        AMOUNT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, set_amount)
        ],
        DESCRIPTION: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, set_description)
        ]
    },
    fallbacks=[CommandHandler("cancel", cancel)]
)

CONFIRM = range(1)


async def clear_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    inline_keyboard = [
        [InlineKeyboardButton("Да", callback_data="clear_yes"),
         InlineKeyboardButton("Нет", callback_data="cancel")]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await update.message.reply_text("Вы уверены?", reply_markup=reply_markup)
    return CONFIRM


async def clear_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "cancel":
        await query.edit_message_text("Операция отменена.")
    elif query.data == "clear_yes":
        user_id = update.effective_user.id
        if sql_components.remove_all_transaction(user_id):
            await query.edit_message_text("История транзакций удалена")
        else:
            await query.edit_message_text("Ошибка удаления истории транзакций.")
    else:
        await query.edit_message_text("Неизвестная команда.")

    return ConversationHandler.END


conv_handler_clear = ConversationHandler(
    entry_points=[
        CommandHandler("clear", clear_start)
    ],
    states={
        CONFIRM: [
            CallbackQueryHandler(clear_confirm)
        ]
    },
    fallbacks=[CommandHandler("cancel", cancel)]
)


# обработчик текста
async def reply_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    buttons_map = {
        "Баланс": balance,
        "История": history,
        "Помощь": help_bot,
    }
    if text in buttons_map:
        await buttons_map[text](update, context)
    else:
        await start(update, context)


def main():
    while not sql_components.create_table():
        time_to_reboot = 5
        print(f"Повторная попытка создания через {time_to_reboot}сек")
        time.sleep(time_to_reboot * 1000)

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("history", history))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(CommandHandler("clear", clear_start))
    app.add_handler(CommandHandler("help", help_bot))
    app.add_handler(conv_handler_add)
    app.add_handler(conv_handler_clear)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_button_handler))

    print("Bot is polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
