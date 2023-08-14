from flask import Blueprint

htmx = Blueprint("htmx", __name__)

@htmx.route("/log-in-button")
def log_in_button():
    return '<a href = ></a>'
