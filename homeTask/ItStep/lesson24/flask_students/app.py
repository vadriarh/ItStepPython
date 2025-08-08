from flask import Flask
from flask_migrate import Migrate

from dotenv import load_dotenv
import os

from models import db
from routes import bp

load_dotenv()
app = Flask(__name__)

# Configuring SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MENU_DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация компонентов
db.init_app(app)  # SQLAlchemy
migrate = Migrate(app, db)  # миграции
app.register_blueprint(bp)  # маршруты
with app.app_context():  # бд
    db.create_all()

# Start app(Flask)
if __name__ == "__main__":
    app.run(debug=True)
