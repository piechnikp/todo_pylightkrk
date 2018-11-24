from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'soSecretThatEvenVoldemortIsScaredToSayIt'

POSTGRES = {
    'user': 'postgres',
    'pw': 'qwerty',
    'db': 'todo',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from project.home.views import home_blueprint
app.register_blueprint(home_blueprint)

from project.api.views import api_blueprint
app.register_blueprint(api_blueprint)

