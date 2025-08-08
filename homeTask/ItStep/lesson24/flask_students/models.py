from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db: SQLAlchemy = SQLAlchemy()


class Student(db.Model):
    __tablename__="students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)
    birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(5), nullable=False)
    course = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return (f"(repr)Student (name:{self.name}, surname: {self.surname}, birthday:{self.birthday}),"
                f" gender:{self.gender}), course:{self.course}),")
