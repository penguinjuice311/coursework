from typing import Protocol
from flask import Blueprint, request


class Database(Protocol):
    pass

def make_auth(database: Database) -> Blueprint:
    auth = Blueprint("auth", __name__)

    @auth.route("/validate_login", methods = ["POST"])
    def validate_login():
        print(request.form["name"])
        return request.form["name"]


    return auth
