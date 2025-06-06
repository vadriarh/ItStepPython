from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes


from homeTask.ItStep.lesson18.telegram_bot_sql.sql_components import *

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN_ID")
ADMIN_ID = int(os.getenv("ADMIN_ID"))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(add_user(user.id, user.username))


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    note = update.message.text[5::]
    add_note(user_id, note)
    await update.message.reply_text(f"Добавлена заметка: {note}")


async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    notes_content = show_notes(user_id)
    if notes_content:
        answer = "Список заметок: \n"
        for note in notes_content:
            answer += f"\t\t\t\t\t{note}\n"
    else:
        answer = "Нет заметок."
    await update.message.reply_text(answer)


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    remove_notes(user.id)
    await update.message.reply_text(f"Все заметки удалены.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    create_table_users()
    create_table_notes()
    create_table_logs()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("notes", notes))
    app.add_handler(CommandHandler("clear", clear))
    print("Bot is polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
