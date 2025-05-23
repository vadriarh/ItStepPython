# ITSTep 2025 Warszawa
# [Ссылка на бот](https://t.me/itstep_waw_2025_telegram_bot)
Телеграм-бот(async) для обработки навыков создания ботов в Telegram при помощи Python 3.13.
В проекте используется личный токен для проверки функционала бота. 
Данный бот обрабатывает запросы в формате /команда текст.

## Содержание
- [Установка](#установка)
- [Использование](#использование)
- [Команды](#команды)
- [Ошибки](#Ошибки)
- [Автор](#Автор)

## Установка
Данный проект в текущий момент не размещается на репозитории, 
а значит требует запуска через виртуальную среду IDE.
Чтобы запустить этот проект, необходимо:

1. Создать проект в IDE PyCharm.
2. Поместить содержимое архива в проект.
3. Выполнить команду в системной консоли IDE: *.venv\Scripts\activate*
4. Установить зависимости через системную команду: *pip install -r requirements.txt*

## Использование
После выполнения установки достаточно только запустить на выполнение файл *bot.py* или команду *python bot.py*. 
После этого бот начнет обработку сообщений.

## Команды
Список доступных команд:
- /start — приветствие
- /help — список команд
- /about — немного о программе
- /time — текущее время
- /echo — повторяет текст
- /reverse — переворачивает фразу
- /status — загрузка системы

## Ошибки
Данный бот выдает предупреждения, если просто ввести команды */echo* и */reverse*.
Бот не обрабатывает просто текст или команды, не указанные в перечне доступных команд.

## Автор
Vadzim Sabadakha 
- PUsb180125 ITStep Warszawa
- Telegram: [@Vlafit](https://t.me/vlafit)

 