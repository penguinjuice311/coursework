from flask import Blueprint, request

auth = Blueprint("auth", __name__)

@auth.route("/validate_login", methods = ["POST"])
def validate_login():
    print(request.form["name"])
    return request.form["name"]

