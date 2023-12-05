from typing import Protocol
from flask import Blueprint, request, render_template


class Database(Protocol):
    pass

class Walker:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        

def make_auth(database: Database) -> Blueprint:
    auth = Blueprint("auth", __name__)

    @auth.route("/validate_login", methods = ["POST"])
    def validate_login():
        print(request.form["name"])
        return request.form["name"]
    
    @auth.route("/search", methods = ["POST", "GET"])
    def search():
        form = request.form
        search = form["search"]
        walkers = [Walker("Kya", "kya@gmail.com"),
                   Walker("connor", "connor@gmail.com"),
                   Walker("smudge", "smudge@gmail.com")]
        walkers_names = ["kya", "connor", "smudge"]
        
        return render_template("search_results.html", search = search, walkers = walkers)

    return auth
