from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MENU_DATABASE')

db = SQLAlchemy(app)


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    img_original_url = db.Column(db.String(255))


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


@app.route("/")
def main():
    return (render_template("index.html"))

@app.route("/hello")
def hello():
    name=request.args.get("name","World")
    age=request.args.get("age","None")
    str = f"Hello, {name}!"
    if age.isdigit():
        str+=f"\nYour age is {age}"
    return str


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


if __name__ == "__main__":
    app.run(debug=True)
