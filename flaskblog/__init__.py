import os #TO USE ENVIRONMENT VARIABLES
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)


app.config['SECRET_KEY'] = 'de74e7b0fad76d362bfd1fcd0c0fd885'
#init db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#we want to tie users to login so that they can only access user account infof if they are logged in
login_manager.login_view = 'login'
#login_message_category is a bootstrap class
login_manager.login_message_category = 'info'
#setting up mail 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] =  587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] =  os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] =  os.environ.get('EMAIL_PASS')


#initializing the mailing extension 
mail = Mail(app)

#IMPORTING ROUTES SO AS TO REGISTER THE INITIALIZED BLUEPRINTS
from flaskblog.main.routes import main
from flaskblog.posts.routes import posts
from flaskblog.users.routes import users

#REGISTERING THE  BLUEPRINTS NOW
app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(users)