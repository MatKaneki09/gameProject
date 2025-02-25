from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booster.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Nécessaire pour utiliser flash messages

db = SQLAlchemy(app)

from fonction.routes import *

if __name__ == "__main__":
    db.create_all()  # Crée toutes les tables à partir des modèles définis
    app.run(debug=True)
