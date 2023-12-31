from typing import Protocol
from flask import Blueprint, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class User(Protocol):
    def get_name(self, email: str) -> str:
        ...

    def is_walker(self, email: str) -> bool:
        ...

    def email_exists(self, email: str) -> bool:
        ...

class LoginForm(FlaskForm):
    email = StringField("email", render_kw = {"placeholder": "email"}, validators = [DataRequired("need an email")])
    password = PasswordField("password", validators = [DataRequired("need an password")])
    submit = SubmitField("Log In")

def make_views(user: User) -> Blueprint:
    user_id = ""
    views = Blueprint("views", __name__)

    @views.route("/", methods = ["GET", "POST"])
    def home():
        login_form = LoginForm()
        if login_form.is_submitted():
            result = request.form
            email = result["email"]
            name = user.get_name(result["email"])
            template = "walker_dashboard.html" if user.is_walker(email) else "owner_dashboard.html"
            return render_template(template, name = name)

        return render_template("home.html", login_form=login_form)

    @views.route("/log-in", methods = ["GET", "POST"])
    def log_in():
        form = LoginForm()
        if form.is_submitted():
            if not user.email_exists():
                #do something
                pass
            result = request.form
            email = result["email"]
            redirect(f"/dashboard/{id}")

        return render_template("log-in.html", form = form)

    @views.route("/sign-up")
    def sign_up():
        return render_template("sign-up.html")

    @views.route("/register")
    def register():
        return render_template("register.html")


    @views.route("/dashboard/<id>")
    def dashboard():
        name = user.get_name(result["email"])
        template = "walker_dashboard.html" if user.is_walker(email) else "owner_dashboard.html"
        return render_template(template, name = name)
        return ""

    @views.route("/profile/<id>")
    def profile(id):
        print(id)
        name = user.get_name(id)
        return render_template("profile.html", name = name)

    return views
