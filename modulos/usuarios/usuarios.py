from flask import Blueprint, render_template, request, redirect, flash
from models import Usuario
from database import db

bp_usuarios = Blueprint('usuarios', __name__, template_folder="templates")

@bp_usuarios.route("/")
def index():
    u = Usuario.query.all()
    return render_template("usuarios.html", dados=u)

@bp_usuarios.route("/add")
def add():
    return render_template("usuarios_add.html")

@bp_usuarios.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    email = request.form.get("email")
    if nome and email:
        db_usuario = Usuario(nome, email)
        db.session.add(db_usuario)
        db.session.commit()
        flash("Usuario cadastrado!")
        return redirect("/usuarios")
    else:
        flash("Preencha todos os campos!")
        return redirect("/usuarios/add")
    
@bp_usuarios.route("/remove/<int:id>")
def remove(id):
    u = Usuario.query.get(id)
    try:
        db.session.delete(u)
        db.session.commit()
        flash("Usuario removido!")
    except:
        flash("Usuario Inválido!")
    return redirect("/usuarios")

@bp_usuarios.route("/edit/<int:id>")
def edit(id):
    u = Usuario.query.get(id)
    return render_template("usuarios_edit.html", dados=u)

@bp_usuarios.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    email = request.form.get("email")
    id = request.form.get("id")
    if nome and email and id:
        u = Usuario.query.get(id)
        u.nome = nome
        u.email = email
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/usuarios")