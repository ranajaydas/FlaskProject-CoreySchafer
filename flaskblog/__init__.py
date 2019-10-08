import os
from flask import Flask                                 # pip install Flask
from flask_sqlalchemy import SQLAlchemy                 # pip install Flask-SQLAlchemy
from flask_bcrypt import Bcrypt                         # pip install Flask-Bcrypt
from flask_login import LoginManager                    # pip install Flask-Login
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '0bbe7a69ad9ecf8eced7a362d7948e4c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'            # Blue-bar message on top when login is required
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from flaskblog import routes