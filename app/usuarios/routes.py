from flask import Blueprint,render_template

usuarios_bp=Blueprint('usuarios',__name__,url_prefix="/usuarios",template_folder="templates")

@usuarios_bp.route("/")
def lista_usuarios():
    return render_template('lista.html')
    #return "<h2>Lista de usuarios</h2>"

@usuarios_bp.route("/perfil/<nombre>")
def perfil(nombre):
    return f"<h3> Perfil del usuario: {nombre} </h3>"