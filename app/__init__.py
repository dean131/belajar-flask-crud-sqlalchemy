from distutils.log import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


# inisiasi flask
app = Flask(__name__)

# config
app.config.from_object(Config)

# inisiasi db
db = SQLAlchemy(app)



from app import routes
from app.models import users

# if __name__ == "__main__":
#     app.run(debug=True)