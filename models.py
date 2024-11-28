from database import db

class Usuario(db.Model):
    __tablename__ = 'tb_usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))


    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


    def __repr__(self):
        return f"<Usuario {self.nome}>"
    

class Postagem(db.Model):
    __tablename__ = 'tb_postagem'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    conteudo = db.Column(db.String(255))
    id_usuario = db.Column(db.Integer, db.ForeignKey('tb_usuario.id'))

    usuario = db.relationship('Usuario', foreign_keys=id_usuario)


    def __init__(self, titulo, conteudo, id_usuario):
        self.titulo = titulo
        self.conteudo = conteudo
        self.id_usuario = id_usuario

    
    def __repr__(self):
        return f"<Postagem {self.titulo} - {self.usuario.nome}>"