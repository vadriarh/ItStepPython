import sqlite3

from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

from validations import *

bp = Blueprint("main", __name__)


@bp.route("/")
def main_page():
    students = Student.query.all()
    return render_template("index.html", students=students)


@bp.route("/add", methods=["GET", "POST"])
def add_student():
    def return_page_template(error: str = None):
        return render_template('add_student.html', error=error)

    if request.method == "GET":
        return render_template('add_student.html')
    if request.method == "POST":
        # Получение данных и уборка "мусора"
        stud_name = (request.form.get("name") or "").strip()
        stud_surname = (request.form.get("surname") or "").strip()
        stud_email = (request.form.get("email") or "").strip()
        stud_birthday_str = (request.form.get("birthday") or "").strip()
        stud_gender = (request.form.get("gender") or "").strip()
        stud_course = (request.form.get("course") or "").strip()

        # Валидация данных
        # Валидация имени
        if not validate_name(stud_name):
            return return_page_template(error="Не введено имя пользователя.")
        # Валидация фамилия
        if not validate_surname(stud_surname):
            return return_page_template(error="Не введена фамилия пользователя.")
        # Валидация повторений студентов
        if not validate_unique_student(stud_name, stud_surname):
            return return_page_template(error="Уже существует студент с этим именем.")
        # Валидация email-а
        check_email = validate_email(stud_email)
        if check_email[0] is None:
            return return_page_template(error=check_email[1])
        # Валидация даты рождения
        if not validate_birthday(stud_birthday_str):
            return return_page_template(error="Неправильно введена дата рождения.")
        # Валидация пола
        if not validate_gender(stud_gender):
            return return_page_template(error="Неправильно введен пол студента.")
        # Валидация курса
        if not validate_course(stud_course):
            return return_page_template(error="Неправильно введен курс обучения.")

        # Сохранение данных в ORM-бд
        stud_birthday = datetime.strptime(stud_birthday_str, "%Y-%m-%d")
        try:
            db.session.add(Student(name=stud_name, surname=stud_surname, email=stud_email,
                                   birthday=stud_birthday, gender=stud_gender, course=stud_course))
            db.session.commit()
        except sqlite3.Error as e:
            return return_page_template(error=str(e))

        # Завершение работы метода
        return redirect(url_for("main.add_student"))
    return render_template('add_student.html')


@bp.route("/delete/<stud_id>")
def delete_student_for_id(stud_id):
    student = db.session.get(Student, stud_id)
    if not student:
        return f"student {stud_id} not found."
    db.session.delete(student)
    db.session.commit()
    return f"student {stud_id} is deleted."


@bp.route("/update/<stud_id>")
def update_student_for_id(stud_id):
    print(stud_id)
    stud_name = validate_name(request.args.get("name"))
    stud_surname = validate_surname(request.args.get("surname"))
    stud_email = validate_email(request.args.get("email"))
    stud_birthday_str = validate_birthday(request.args.get("birthday")),
    stud_gender = validate_gender(request.args.get("gender"))
    stud_course = validate_course(request.args.get("course"))

    stud_birthday = datetime.strptime(str(stud_birthday_str), "%Y-%m-%d")
    student = db.session.get(Student, stud_id)
    if not validate_unique_student(stud_name, stud_surname):
        return f"student with id{stud_id} not found."
    if stud_name:
        student.name = stud_name
    if stud_surname:
        student.surname = stud_surname
    if stud_email:
        student.email = stud_email
    if stud_birthday:
        student.birthday = stud_birthday
    if stud_gender:
        student.gender = stud_gender
    if stud_course:
        student.course = stud_course

    db.session.commit()
    return f"student id:{stud_id} is updated."
