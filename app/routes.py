from app import app
from flask import request
from app.controller import userController

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return userController.tampilUsers()
    else:
        return userController.tambahUser()

@app.route("/users/<id>", methods=["GET", "PUT", "DELETE"])
def userDetail(id):
    if request.method == "GET":
        return userController.tampilUser(id)
    elif request.method == "PUT":
        return userController.updateUser(id)
    elif request.method == "DELETE":
        return userController.hapusUser(id)

@app.route('/login')
def login():
    email = request.args.get('email')
    password = request.args.get('password')

    return f'email= {email}\npassword= {password}'
