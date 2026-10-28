from flask import Blueprint,render_template

blog_bp=Blueprint('blog',__name__,url_prefix="/entrada",template_folder="templates")

@blog_bp.route("/<int:id>")
def entrada(id):
    titulo_dinamico = f"entrada numero {id}"
    return render_template('blog.html', titulo=titulo_dinamico)