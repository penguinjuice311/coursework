from flask import Blueprint, render_template

views = Blueprint("views", __name__)

owners = ["connor", "kya", "finn"]

walkers = ["louise", "john", "martha"]

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/log-in")
def log_in():
    return render_template("log-in.html")

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
