from typing import Protocol
from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class User(Protocol):
    def get_name(email: str) -> str:
        ...

    def is_walker(email: str) -> bool:
        ...

class LoginForm(FlaskForm):
    email = StringField("email")
    password = PasswordField("password")
    submit = SubmitField("Log In")

def make_views(user: User) -> Blueprint:
    views = Blueprint("views", __name__)

    owners = ["connor", "kya", "finn"]

    walkers = ["louise", "john", "martha"]

    @views.route("/")
    def home():
        return render_template("home.html")

    @views.route("/log-in", methods = ["GET", "POST"])
    def log_in():
        form = LoginForm()
        if form.is_submitted():
            result = request.form
            email = result["email"]
            name = user.get_name(result["email"])
            template = "walker_dashboard.html" if user.is_walker(email) else "owner_dashboard.html"
            return render_template(template, name = name)
        return render_template("log-in.html", form = form)

    @views.route("/sign-up")
    def sign_up():
        return render_template("sign-up.html")

    @views.route("/register")
    def register():
        return render_template("register.html")


    @views.route("/dashboard/<id>")
    def dashboard():
        return ""

    @views.route("/profile/<id>")
    def profile():
        return ""

    return views
