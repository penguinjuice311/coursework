from flask import Flask
from .user import User
from .database import Database
from .dud_sql import Sql
from .auth import make_auth
from .views import make_views
from .input_validation import make_input_validation
from .validator import Validator


def create_app(constring):
    app = Flask(__name__)
    
    sql = Sql(constring)

    database = Database(sql)
    user = User()
    validator = Validator()
    
    app.register_blueprint(make_views(User()))
    app.register_blueprint(make_auth(Database(sql)), url_prefix = "/auth")
    app.register_blueprint(make_input_validation(validator, user), url_prefix = "/validation")

    return app
