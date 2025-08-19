from datetime import timedelta

from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from models import db, Dish
from routes import bp
from handlers import init_jwt_handlers

from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# ORM-connection with SQLALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MENU_DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=2)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=7)

# Инициализация компонентов
db.init_app(app)  # SQLAlchemy
migrate = Migrate(app, db)  # миграции
app.register_blueprint(bp)  # маршруты
init_jwt_handlers(app)  # jwt-обработчики

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
