from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = '42c75396af1d6fe606131f7da21191ff3ef10f5a0cda55bf3246d868341de540'

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/atividade_db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from database import db
from flask_migrate import Migrate
from models import Usuario, Postagem

db.init_app(app)
migrate = Migrate(app, db)

from modulos.usuarios.usuarios import bp_usuarios
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

from modulos.postagens.postagens import bp_postagens
app.register_blueprint(bp_postagens, url_prefix='/postagens')

@app.route("/")
def index():
    return render_template("index.html")