from flask import Flask, render_template, request, redirect, url_for, g
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from model import *

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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Инициализация SQLAlchemy
migrate = Migrate(app, db)  # Инициализация миграций


# ORM Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(25), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"(repr)User (name:{self.name}, surname: {self.surname}, age:{self.year})"

    # def __str__(self):
    #     return f"(str)User ({self.name}, age:{self.year})"


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


# Initializing and adding in database, when is empty
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
    # fmt off
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
    mdb.execute("""
                CREATE TABLE IF NOT EXISTS comment
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    stars INTEGER NOT NULL,
                    comment TEXT
                )
                """)

    # fmt on
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
        user = mdb.execute("SELECT * FROM authorize WHERE login = ?", (login,)).fetchone()
        # finally checking userdata
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
    mdb = get_db()

    # Получение списка уже имеющихся отзывов
    def get_old_comments():
        # Отслеживание фильтрации
        rating_select = (request.form.get("rating-select") or "").strip() or None
        # Построение SQL-query
        sql_query = "SELECT * FROM comment"
        # Проверки фильтра рейтинга
        try:
            validate_rating_select = (rating_select and
                                      int(rating_select) in range(1, 6))
        except ValueError:
            validate_rating_select = False
        # Запрос отфильтрованных записей
        if validate_rating_select:
            sql_query += f" WHERE stars = ?"
            comments_raw = mdb.execute(sql_query, (rating_select,)).fetchall()
        else:
            comments_raw = mdb.execute(sql_query).fetchall()

        comments = [dict(row) for row in comments_raw]
        # Получение средней общей оценки
        avg_stars_raw = mdb.execute("SELECT AVG(stars) FROM comment").fetchone()
        avg_stars = round(avg_stars_raw[0], 2) if (avg_stars_raw[0] is not None) else None
        return comments, avg_stars

    # Создание шаблона
    def return_comment_template(error: str = None):
        comments, avg_stars = get_old_comments()
        return render_template('comments.html', error=error, comments=comments, avg_stars=avg_stars)

    if request.method == "GET":
        return return_comment_template()
    if request.method == "POST":
        # Получение данных и уборка "мусора"
        username = (request.form.get("username") or "").strip()
        email = (request.form.get("email") or "").strip()
        stars_raw = request.form.get("stars")
        comment = (request.form.get("comment") or "").strip() or None
        # Валидация данных
        # Валидация имени
        if not username:
            return return_comment_template(error="Не введено имя пользователя.")
        # Валидация email-а
        if not email or "@" not in email:
            return return_comment_template(error="Неправильно введенный email.")
        # Валидация рейтинга
        if not stars_raw:
            return return_comment_template(error="Не выбрана оценка.")
        try:
            stars = int(stars_raw)
            if stars not in range(1, 6):
                return return_comment_template(error="Рейтинг вне диапазона 1–5")
        except ValueError:
            return return_comment_template(error="Ошибка ввода значения оценки.")

        # Валидация комментария
        # if not comment:
        #     error = "Пустое поле для отзыва."
        #     return render_template('comments.html', error=error)

        # Сохранение данных в ORM-бд
        # db.session.add(Comment(name=username, email=email, stars=stars, comment=comment))
        # db.session.commit()

        # Сохранение данных в Manual-бд
        mdb.execute("INSERT INTO comment (name, email, stars, comment) VALUES (?, ?, ?, ?)",
                    (username, email, stars, comment))
        mdb.commit()
        # Завершение работы метода
        return redirect(url_for("send_comment"))
    return return_comment_template()


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

#  CRUD-interface USER
@app.route("/add_user")
def add_user():
    name = request.args.get("name")
    year = request.args.get("year")
    surname = request.args.get("surname")
    user = User(name=name, year=year, surname=surname)
    db.session.add(user)
    db.session.commit()
    return str(user)
    # return f"User {name}, year: {year}"

@app.route("/update_user")
def update_user():
    id = request.args.get("id")
    name = request.args.get("name")

    user = db.session.get(User,id)
    if not user:
        return f"User {id} not found."
    user.name = name
    db.session.commit()
    return f"User {id} is updated."

@app.route("/delete_user")
def delete_user():
    id = request.args.get("id")
    user = db.session.get(User,id)
    if not user:
        return f"User {id} not found."
    db.session.delete(user)
    db.session.commit()
    return f"User {id} is deleted."



@app.route("/users")
def show_users():
    users = User.query.all()
    return "<br>".join(f"{user.id}. {user.name} {user.surname} - {user.year} years old" for user in users)

@app.route("/menu")
def menu():
    dishes = Dish.query.all()
    return render_template("menu.html", dishes=dishes)


# Start app(Flask)
if __name__ == "__main__":
    app.run(debug=True)
