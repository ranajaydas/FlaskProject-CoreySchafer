from flask import Flask                                 # pip install Flask
from flask_sqlalchemy import SQLAlchemy                 # pip install Flask-SQLAlchemy
from flask_bcrypt import Bcrypt                         # pip install Flask-Bcrypt
from flask_login import LoginManager                    # pip install Flask-Login


app = Flask(__name__)
app.config['SECRET_KEY'] = '0bbe7a69ad9ecf8eced7a362d7948e4c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'            # Blue-bar message on top when login is required


from flaskblog import routes