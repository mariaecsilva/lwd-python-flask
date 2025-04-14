from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Register(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    price = db.Column(db.Float)
    time = db.Column(db.Float)

    def __init__(self, title, price, time):
        self.title = title
        self.price = price
        self.time = time

class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, filename):
        self.filename = filename