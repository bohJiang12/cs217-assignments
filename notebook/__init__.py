# Import dependency map: `routes` <- `notes` <- `model`


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# TODO: app config

# Init a database model for the app
# db = SQLAlchemy(app)
db = SQLAlchemy()
from notebook import routes
from notebook import notes