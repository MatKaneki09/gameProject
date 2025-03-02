from app import db

class User(db.Model):
    iduser = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    collection = db.relationship('Collection', backref='owner', lazy=True)

class Collection(db.Model):
    idcollection = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.iduser'), nullable=False)
    cartes = db.relationship('Carte_Collection', backref='collection', lazy=True)

class Carte(db.Model):
    idcarte = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

class Carte_Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idcollection = db.Column(db.Integer, db.ForeignKey('collection.idcollection'), nullable=False)
    idcarte = db.Column(db.Integer, db.ForeignKey('carte.idcarte'), nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
