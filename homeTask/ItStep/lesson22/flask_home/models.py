from email.policy import default

from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()


class Dish(db.Model):
    __tablename__ = "dishes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    img_original_url = db.Column(db.String(255))


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(25))
    years = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"(repr)User (name:{self.name}, surname: {self.surname}, age:{self.years})"

    # def __str__(self):
    #     return f"(str)User ({self.name}, age:{self.year})"


class Security(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(175), nullable=False)
    role = db.Column(db.String(25), default="user")
