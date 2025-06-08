import homeTask.ItStep.lesson18.telegram_bot_sql.sql_components as sql_components
import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes, filters, MessageHandler

from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN_ID")
ADMIN_ID = int(os.getenv("ADMIN_ID"))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    reply_keyboard = [["Показать все заметки", "Удалить все заметки"], ["Помощь"]]
    reply_markup = ReplyKeyboardMarkup(
        reply_keyboard,
        resize_keyboard=True,
        one_time_keyboard=False)
    await update.message.reply_text(sql_components.add_user(user.id, user.username), reply_markup=reply_markup)


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    note = update.message.text.removeprefix("/add ")
    if sql_components.add_note(user_id, note):
        await update.message.reply_text(f"Добавлена заметка: {note}")
    else:
        await update.message.reply_text("Превышен лимит доступных слотов. Необходимо удалить заметки.")


async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    notes_content = sql_components.show_notes(user_id)
    if notes_content:
        result_list = '\n'.join(item[0] for item in notes_content)
        answer = f"Список заметок:\n{result_list}"
    else:
        answer = "Нет заметок."
    await update.message.reply_text(answer)


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    sql_components.remove_notes(user.id)
    await update.message.reply_text(f"Все заметки удалены.")


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id == ADMIN_ID:
        target_note = update.message.text.removeprefix("/search ")
        list_users = sql_components.search_note(target_note)
        if list_users:
            result_list = '\n'.join(str(item[0]) for item in list_users)
            await update.message.reply_text(
                f"Список пользователей у кого есть эта "
                f"заметка ({target_note}):\n{result_list}")
        else:
            await update.message.reply_text(f"Пользователи отсутствуют.")

    else:
        await update.message.reply_text("Данная команда доступна только Администратору.")


async def limit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id == ADMIN_ID:
        new_limit = int(update.message.text.removeprefix("/limit "))
        sql_components.change_limit_slots(new_limit)
        await update.message.reply_text(f"Число слотов для заметок изменен на {new_limit}")
    else:
        await update.message.reply_text("Данная команда доступна только Администратору.")


async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id == ADMIN_ID:
        list_users = sql_components.get_users()
        if list_users:
            result_list = '\n'.join((str(item) for item in list_users))
            await update.message.reply_text(f"Список всех пользователей: \n"
                                            f"{result_list}")
        else:
            await update.message.reply_text(f"Пользователи отсутствуют.")

    else:
        await update.message.reply_text("Данная команда доступна только Администратору.")


async def reply_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    buttons_map = {
        "Показать все заметки": notes,
        "Удалить все заметки": clear,
        "Помощь": help_bot,
    }
    if text in buttons_map:
        await buttons_map[text](update, context)
    else:
        await add(update, context)


async def help_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (f"Данный бот работает с командами (без круглых скобок):\n"
               f"       /add (новая заметка)    - добавляет новую заметку\n"
               f"       /notes                  - показывает список всех заметок\n"
               f"       /clear                  - удаляет ВСЕ заметки\n"
               f"       /help                   - помощь\n"
               f"Текст, введённый без команд, рассматривается как добавленная заметка.")
    await update.message.reply_text(message)


def main():
    sql_components.create_table_users()
    sql_components.create_table_notes()
    sql_components.create_table_logs()

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("notes", notes))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("search", search))
    app.add_handler(CommandHandler("limit", limit))
    app.add_handler(CommandHandler("users", users))
    app.add_handler(CommandHandler("help", help_bot))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_button_handler))

    print("Bot is polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
