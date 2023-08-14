from flask import Flask
from .auth import auth
from .views import views
from .htmx import htmx


def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(views)
    app.register_blueprint(auth, url_prefix = "/auth")
    app.register_blueprint(htmx, url_prefix = "/htmx")

    return app
