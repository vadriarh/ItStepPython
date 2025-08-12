from flask import Flask, render_template, request, redirect, url_for, g, jsonify
from flask_migrate import Migrate

from models import db, Dish

from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)


# ORM-connection with SQLALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MENU_DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)  # Инициализация миграций

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


# Start app(Flask)
if __name__ == "__main__":
    app.run(debug=True)
