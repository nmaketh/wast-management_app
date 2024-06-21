from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory containing the current file
current_directory = os.path.dirname(current_file_path)

# Create a Flask app and provide the path to the directory containing the templates directory
app = Flask(__name__, template_folder=current_directory + '/templates')

#db connection
app.secret_key='sjbit'

# Create the path for the database file
database_file_path = os.path.join(current_directory, 'test.db')

# Use the path for the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file_path

db=SQLAlchemy(app)

login_manager=LoginManager(app)
login_manager.login_view='login'

# Import routes after the Flask app is created