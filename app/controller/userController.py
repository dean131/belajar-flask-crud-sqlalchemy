from app import response, db
from flask import request
from app.models.users import Users

def tampilUsers():
    try:
        users = Users.query.all()
        data = ubahKeArray(users)
        return response.ok(data, "Berhasil ambil data")
    except Exception as e:
        print(e)

def tampilUser(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest("","User tidak ditemukan")
        data = {
            "id" : user.id,
            "nama" : user.nama,
            "email" : user.email,
            "password" : user.password,
            "alamat" : user.alamat,
            "j_kelamin" : user.j_kelamin,
            "no_telp" : user.no_telp,
            "dibuat" : user.dibuat
        }
        return response.ok(data, "User barhasil ditemukan")
    except Exception as e:
        print(e)

def ubahKeArray(users):
    arrayUsers = []
    for user in users:
        arrayUsers.append({
                "id" : user.id,
                "nama" : user.nama,
                "email" : user.email,
                "password" : user.password,
                "alamat" : user.alamat,
                "j_kelamin" : user.j_kelamin,
                "no_telp" : user.no_telp,
                "dibuat" : user.dibuat
            })
    return arrayUsers

def tambahUser():
    try:
        dnama = request.form["nama"]
        demail = request.form["email"]
        dpassword = request.form["password"]
        dalamat = request.form["alamat"]
        dj_kelamin = request.form["j_kelamin"]
        dno_telp = request.form["no_telp"]
        user = Users(
            nama = dnama, 
            email = demail, 
            password = dpassword, 
            alamat = dalamat, 
            j_kelamin = dj_kelamin, 
            no_telp = dno_telp
            )
        db.session.add(user)
        db.session.commit()
        return response.ok('', "Berhasil menambah data")
    except Exception as e:
        print(e)

def updateUser(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest("", "User tidak ditemukan")
        user.nama = request.json["nama"]
        user.email = request.json["email"]
        user.password = request.json["password"]
        user.alamat = request.json["alamat"]
        user.j_kelamin = request.json["j_kelamin"]
        user.no_telp = request.json["no_telp"]
        db.session.commit()
        return response.ok("", "Berhasil mengupdate")
    except Exception as e:
        print(e)

def hapusUser(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest("", "User tidak ditemukan")
        db.session.delete(user)
        db.session.commit()
        return response.ok('', "Behasil menghapus user")
    except Exception as e:
        print(e)

def validasiLogin(inp_email, inp_pass):
    try:

        user = (Users.query.filter(Users.email==inp_email).filter(Users.password==inp_pass))

        if not user:
            return response.badRequest('', 'user tidak ditemukan')
        data = {
            'email' : inp_email,
            'password' : inp_pass
        }
        return response.ok(data, 'login valid')
    except Exception as e:
        print(e)