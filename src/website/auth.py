from typing import Protocol
from flask import Blueprint, request, render_template


class Database(Protocol):
    pass

def make_auth(database: Database) -> Blueprint:
    auth = Blueprint("auth", __name__)

    @auth.route("/validate_login", methods = ["POST"])
    def validate_login():
        print(request.form["name"])
        return request.form["name"]
    
    @auth.route("/search", methods = ["POST", "GET"])
    def search():
        form = request.form
        for k, v in form.items():
            print(k, v)

        return "searching"

    return auth
