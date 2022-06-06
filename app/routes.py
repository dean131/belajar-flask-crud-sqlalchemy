from app import app
from flask import request
from app.controller import userController

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return userController.tampilUsers()
    else:
        return userController.tambahUser()
