# Import dependency map: `routes` <- `notes` <- `model`


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

# Init a database model for the app
# db = SQLAlchemy(app)
db = SQLAlchemy()
db.init_app(app)

from notebook import routes
from notebook import notes
