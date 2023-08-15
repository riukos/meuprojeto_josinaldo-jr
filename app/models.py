from app import app, db

class ContatoModels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    phone = db.Column(db.String(14), nullable = False)
    message = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return f'<Contato {self.name}>'
    

class CadastroModels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(40), nullable = False, unique = True)
    password = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return f'<Cadastro {self.name}>'