from main import db

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(15), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    altura = db.Column(db.String(5), nullable=False) 

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String(15), primary_key=True)
    nome = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name