import re
from models import db, Student
from sqlalchemy import and_


def validate_name(name: str):
    return name if name else None


def validate_surname(surname: str):
    return surname if surname else None


def validate_email(email: str):
    if not email or "@" not in email:
        return [None,"Email не корректный"]
    if db.session.query(Student).filter(Student.email == email).first():
        return [None,"Email уже занят"]
    return [email]


def validate_birthday(birthday: str):
    if re.match("([0-9][0-9][0-9][0-9])-(0[0-9]|1[0-2])-(0[0-9]|1[0-9]|2[0-9]|3[0-1])", birthday):
        return birthday
    return None


def validate_gender(gender: str):
    genders = ["Male", "Female", "male", "female"]
    return None if gender not in genders else gender


def validate_course(course: str):
    try:
        if int(course) in range(1, 6):
            return course
        else:
            return None
    except ValueError:
        return None


def validate_unique_student(name: str, surname: str):
    student = db.session.query(Student).filter(
        and_(Student.name == name, Student.surname == surname)
    ).first()
    return False if student else True
