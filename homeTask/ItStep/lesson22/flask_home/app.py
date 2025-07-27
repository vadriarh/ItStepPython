from flask import Flask, render_template, request, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()
app = Flask(__name__)

# Manual database management
manual_database = "instance/menu.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(manual_database)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error):
    mdb = g.pop("db", None)
    if mdb is not None:
        mdb.close()


# ORM-connection with SQLALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MENU_DATABASE')

db = SQLAlchemy(app)


# ORM Models
class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    img_original_url = db.Column(db.String(255))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    email = db.Column(db.String(25))
    stars = db.Column(db.Integer)
    comment = db.Column(db.Text)


# Adding in database, when is empty
with app.app_context():
    db.create_all()
    if not Dish.query.first():
        db.session.add(Dish(name="Паста", description="Сливочный соус", price=25,
                            img_original_url="original_pasta.jpg"))
        db.session.add(Dish(name="Пицца", description="Сыр и грибы", price=30,
                            img_original_url="original_pizza.jpg"))
        db.session.add(Dish(name="Салат", description="Овощи и соус", price=15,
                            img_original_url="original_salad.jpg"))
        db.session.commit()


# Routes
@app.route("/")
def main():
    # Получение подключения к базе данных
    mdb = get_db()
    mdb.execute("""
                CREATE TABLE IF NOT EXISTS users
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
                """)
    # Создание таблицы users, если она не существует
    mdb.execute("""
                CREATE TABLE IF NOT EXISTS authorize
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
                """)
    mdb.commit()  # Сохранение изменений в базе данных
    return render_template("index.html")


@app.route("/hello")
def hello():
    name = request.args.get("name", "World")
    age = request.args.get("age", "None")
    str = f"Hello, {name}!"
    if age.isdigit():
        str += f"\nYour age is {age}"
    return str


@app.route("/form")
def form():
    name = request.args.get("name")
    age = request.args.get("age")
    str = f"Hello, {name}!"
    if age:
        str += f"\nYour age is {age}"
        return str
    return render_template("form.html")


@app.route("/info")
def info():
    name = request.args.get("name")
    city = request.args.get("city")
    dish = request.args.get("dish")
    str = f"My name is {name}.\n"
    str += f"My city is {city}.\n"
    str += f"My dish is {dish}."
    return str


@app.route("/register", methods=["GET", "POST"])
def form_reg():
    if request.method == "GET":
        return render_template('reg_form.html')
    if request.method == "POST":
        # get userdata
        login = request.form.get("login")
        password = request.form.get("password")
        # validate input userdata
        mdb = get_db()
        if not login or not password:
            error = "Please fill in all fields."
            return render_template('reg_form.html', error=error)
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
            return render_template('reg_form.html', error=error)
        # trying input userdata in bd
        try:
            mdb.execute("INSERT INTO authorize (login, password) VALUES (?, ?)", (login, password))
            mdb.commit()
            return "Новый пользователь зарегистрирован."
        except sqlite3.IntegrityError as e:
            error = f"Ошибка сохранения: {e}"
            return render_template('reg_form.html', error=error)
    return render_template('reg_form.html')


@app.route("/login", methods=["GET", "POST"])
def form_log():
    if request.method == "GET":
        return render_template('login_form.html')
    if request.method == "POST":
        # get userdata
        login = request.form.get("login")
        password = request.form.get("password")
        # validate input userdata
        if not login or not password:
            error = "Please fill in all fields."
            return render_template('login_form.html', error=error)
        # check userdata into bd
        mdb = get_db()
        user = mdb.execute("SELECT * FROM authorize WHERE login = ?", (login, )).fetchone()
        #finally checking userdata
        if user:
            if user["password"] == password:
                return f"Добро пожаловать, {login}."
            error = "Пароли не совпадают."
            return render_template('login_form.html', error=error)
        else:
            error = "Такого пользователя не существует."
            return render_template('login_form.html', error=error)
    return render_template('login_form.html')


@app.route("/comments", methods=["GET", "POST"])
def send_comment():
    if request.method == "GET":
        return render_template("comments.html")
    if request.method == "POST":
        # Получение данных
        username = request.form.get("username")
        email = request.form.get("email")
        stars = request.form.get("stars")
        comment = request.form.get("comment")
        # Валидация данных
        # Валидация рейтинга
        if not stars:
            error = "Не выбрана оценка."
            return render_template('comments.html', error=error)
        stars = int(stars)
        if stars not in range(1, 6):
            error = "Оценка может быть в диапазоне от 1 до 5."
            return render_template('comments.html', error=error)
        # Валидация email-а
        if not email or "@" not in email:
            error = "Неправильно введенный email."
            return render_template('comments.html', error=error)
        # Валидация комментария
        if not comment:
            error = "Пустое поле для отзыва."
            return render_template('comments.html', error=error)
        # Сохранение данных в бд
        db.session.add(Comment(name=username, email=email, stars=stars, comment=comment))
        db.session.commit()
        # Завершение работы метода
        message = f"Спасибо за отзыв, {username}"
        return render_template('comments.html', message=message)
    return render_template('comments.html')


@app.route("/nav")
def nav():
    if request.args.get("name"):
        return redirect("/info")
    return render_template("navigation.html")


@app.route("/about")
def about():
    contacts = {'address': os.getenv("CONTACT_ADDRESS"), 'email': os.getenv("CONTACT_EMAIL"),
                'facebook': os.getenv("CONTACT_FACEBOOK"), 'instagram': os.getenv("CONTACT_INSTAGRAM"),
                'phone': os.getenv("CONTACT_PHONE")}

    return render_template("about.html", contacts=contacts)


@app.route("/menu")
def menu():
    dishes = Dish.query.all()
    return render_template("menu.html", dishes=dishes)


# Start app(Flask)
if __name__ == "__main__":
    app.run(debug=True)
