from flask import Blueprint, render_template, request, redirect, flash
from models import Postagem, Usuario
from database import db

bp_postagens = Blueprint('postagens', __name__, template_folder="templates")

@bp_postagens.route("/")
def index():
    p = Postagem.query.all()
    return render_template("postagens.html", dados=p)


@bp_postagens.route("/add")
def add():
    p = Postagem.query.all()
    u = Usuario.query.all()
    return render_template("postagens_add.html", dados=p, usuarios=u)


@bp_postagens.route("/save", methods=['POST'])
def save():
    titulo = request.form.get("titulo")
    conteudo = request.form.get("conteudo")
    id_usuario = request.form.get("id_usuario")

    usuario = Usuario.query.all()

    if titulo and conteudo and id_usuario:
        db_postagem = Postagem(titulo, conteudo, id_usuario)
        db.session.add(db_postagem)
        db.session.commit()
        flash("Postagem cadastrada!")
        return redirect("/postagens")
    else:
        flash("Preencha todos os campos!")
        return redirect("/postagens/add")
    

@bp_postagens.route("/remove/<int:id>")
def remove(id):
    p = Postagem.query.get(id)
    try:
        db.session.delete(p)
        db.session.commit()
        flash("Postagem removida!")
    except:
        flash("Postagem Inválida!")
    return redirect("/postagens")


@bp_postagens.route("/edit/<int:id>")
def edit(id):
    p = Postagem.query.get(id)
    u = Usuario.query.all()
    return render_template("postagens_edit.html", dados=p, usuarios=u)


@bp_postagens.route("/edit-save", methods=['POST'])
def edit_save():
    titulo = request.form.get("titulo")
    conteudo = request.form.get("conteudo")
    id_usuario = request.form.get("id_usuario")
    id = request.form.get("id")
    if titulo and conteudo and id_usuario and id:
        p = Postagem.query.get(id)
        p.titulo = titulo
        p.conteudo = conteudo
        p.id_usuario = id_usuario
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/postagens")