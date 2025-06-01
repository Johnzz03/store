from flask import Flask
from flask_migrate import Migrate
from db import db  # Import db from db.py
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/ordering'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize db with app
migrate = Migrate(app, db)

from models import *  # Import models after db is initialized
from routes import main
from routes.user_routes import user_main
from routes.chat_routes import chat_main

app.register_blueprint(main)
app.register_blueprint(user_main)
app.register_blueprint(chat_main)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 4000)))