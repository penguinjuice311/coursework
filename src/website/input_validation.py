from typing import Protocol
from flask import Blueprint, request

class Validator(Protocol):
    pass

class User(Protocol):
    def login(self, email: str, phone_number: str, name: str, password: str):
        ...

def make_input_validation(validator: Validator, user: User):
    input_validation = Blueprint("validator", __name__)

    @input_validation.route("/validate-login", methods = ["POST"])
    def validate_login():
        print(request.form["name"])
        return "Done."

    return input_validation
