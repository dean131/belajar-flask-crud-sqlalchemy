from email.policy import default
from msilib.schema import Class

from sqlalchemy import Column
from app import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    alamat = db.Column(db.TEXT, nullable=True)
    j_kelamin = db.Column(db.String(10), nullable=True)
    no_telp = db.Column(db.String(30), nullable=True)
    dibuat = db.Column(db.DateTime, default=datetime.utcnow)