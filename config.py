import os

basedir = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    database = "sqlite:///" + os.path.join(basedir, "db.sqlite")

    SQLALCHEMY_DATABASE_URI = database
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_RECORD_QUERIES = True