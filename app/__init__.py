from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads/'
app.config['SECRET_KEY'] = "durant35"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gtsnwlterzfxni:82e02b2508e7ffa6e759755cf05221e71a0c39a211d99e713e5b1131c155f4d6@ec2-54-83-58-222.compute-1.amazonaws.com:5432/dff6v16bdg5nfv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views

