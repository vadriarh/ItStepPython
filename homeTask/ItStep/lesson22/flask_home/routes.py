import sqlite3
import os

from flask import Blueprint, render_template, request, redirect, url_for, jsonify, func
from models import *

bp = Blueprint("main", __name__)


@bp.route("/")
def main():
    return render_template("index.html")


@bp.route("/hello")
def hello():
    name = request.args.get("name", "World")
    age = request.args.get("age", "None")
    message = f"Hello, {name}!"
    if age.isdigit():
        message += f"\nYour age is {age}"
    return message


@bp.route("/form")
def form():
    name = request.args.get("name")
    age = request.args.get("age")
    message = f"Hello, {name}!"
    if age:
        message += f"\nYour age is {age}"
        return message
    return render_template("form.html")


@bp.route("/info")
def info():
    name = request.args.get("name")
    city = request.args.get("city")
    dish = request.args.get("dish")
    message = f"My name is {name}.\n"
    message += f"My city is {city}.\n"
    message += f"My dish is {dish}."
    return message


@bp.route("/register", methods=["GET", "POST"])
def form_reg():
    if request.method == "GET":
        return render_template('reg_form.html')
    if request.method == "POST":
        # get userdata
        login = request.form.get("login")
        password = request.form.get("password")
        # validate input userdata
        if not login or not password:
            error = "Please fill in all fields."
            return render_template('reg_form.html', error=error)
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
            return render_template('reg_form.html', error=error)
        # trying input userdata in bd
        try:
            db.session.add(Login(login=login, password=password))
            db.session.commit()
            return "Новый пользователь зарегистрирован."
        except sqlite3.IntegrityError as e:
            error = f"Ошибка сохранения: {e}"
            return render_template('reg_form.html', error=error)
    return render_template('reg_form.html')


@bp.route("/login", methods=["GET", "POST"])
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
        user = db.session.query(Login).filter(Login.login == login).first()
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


@bp.route("/comments", methods=["GET", "POST"])
def send_comment():
    # Получение списка уже имеющихся отзывов
    def get_old_comments():
        # Отслеживание фильтрации
        rating_select = (request.form.get("rating-select") or "").strip() or None
        # Проверки фильтра рейтинга
        try:
            validate_rating_select = (rating_select and
                                      int(rating_select) in range(1, 6))
        except ValueError:
            validate_rating_select = False
        # Запрос отфильтрованных записей
        comments_raw = db.session.query(Comment).filter(Comment.stars == int(rating_select)).all()
        comments = [dict(row) for row in comments_raw]
        # Получение средней общей оценки
        avg_stars_raw = db.session.query(func.avg(Comment.rating)).scalar()
        avg_stars = round(avg_stars_raw, 2) if (avg_stars_raw is not None) else None
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
        if not comment:
            error = "Пустое поле для отзыва."
            return render_template('comments.html', error=error)

        # Сохранение данных в ORM-бд
        db.session.add(Comment(name=username, email=email, stars=stars, comment=comment))
        db.session.commit()

        # Завершение работы метода
        return redirect(url_for("send_comment"))
    return return_comment_template()


@bp.route("/nav")
def nav():
    if request.args.get("name"):
        return redirect("/info")
    return render_template("navigation.html")


@bp.route("/about")
def about():
    contacts = {'address': os.getenv("CONTACT_ADDRESS"), 'email': os.getenv("CONTACT_EMAIL"),
                'facebook': os.getenv("CONTACT_FACEBOOK"), 'instagram': os.getenv("CONTACT_INSTAGRAM"),
                'phone': os.getenv("CONTACT_PHONE")}

    return render_template("about.html", contacts=contacts)


#  CRUD-interface USER
@bp.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        users = User.query.all()

        return jsonify(
            ([{"id": user.id, "name": user.name, "surname": user.surname, "year": user.year} for user in users]), 200)
    if request.method == "POST":
        data = request.get_json()
        if not "name" in data.keys() or not "year" in data.keys():
            return jsonify({"error": "Bad request."}, 400)
        user = User(name=data["name"], year=data["year"], surname=data["surname"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User added successfully!"}, 201)
    return None


# return f"User {name}, year: {year}"

@bp.route("/update_user", methods=["PUT", "PATCH"])
def update_user():
    data = request.get_json()
    user = db.session.get(User, data.get("id"))
    if not user:
        return jsonify({"error": "Bad id request."}, 400)
    name = data.get("name")
    surname = data.get("surname")
    year = data.get("year")
    if request.method == "PUT":
        if name and surname and year:
            user.name = name
            user.surname = surname
            user.year = year
        else:
            return jsonify({"error": "Bad  put request."}, 400)
    elif request.method == "PATCH":
        if not name and not surname and not year:
            return jsonify({"error": "Bad patch request."}, 400)
        if name:
            user.name = name
        if surname:
            user.surname = surname
        if year:
            user.year = year
    db.session.commit()
    return jsonify({"message": f"User id{user.id} updated"}, 201)


@bp.route("/delete_user")
def delete_user():
    user_id = request.args.get("id")
    user = db.session.get(User, user_id)
    if not user:
        return f"User {user_id} not found."
    db.session.delete(user)
    db.session.commit()
    return f"User {user_id} is deleted."


@bp.route("/users")
def show_users():
    users = User.query.all()
    return "<br>".join(f"{user.id}. {user.name} {user.surname} - {user.birthday} years old" for user in users)


@bp.route("/menu")
def menu():
    dishes = Dish.query.all()
    return render_template("menu.html", dishes=dishes)
