from app import app, response
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

@app.route('/login', methods=['GET'])
def loginUser():

    if request.method == "GET":
        inp_email = request.args.get('email')
        inp_pass = request.args.get('password')
        return userController.authLogin(inp_email, inp_pass)
    else:
        return response.badRequest('', 'url tidak valid')

