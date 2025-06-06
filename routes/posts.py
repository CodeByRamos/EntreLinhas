from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, current_app
from datetime import datetime
import database as db

# Criação do Blueprint para as rotas de posts (desabafos)
posts = Blueprint('posts', __name__)

@posts.route('/feed')
def feed():
    """Rota para a página de feed de desabafos."""
    desabafos = db.get_posts()
    categorias = current_app.config['CATEGORIAS']
    reacoes = current_app.config['REACOES']
    return render_template('feed.html', desabafos=desabafos, categorias=categorias, reacoes=reacoes)

@posts.route('/enviar', methods=['POST'])
def enviar():
    """Rota para enviar um novo desabafo."""
    if request.method == 'POST':
        conteudo = request.form.get('conteudo')
        categoria = request.form.get('categoria')
        
        if not conteudo or not categoria:
            flash('Por favor, preencha todos os campos.')
            return redirect(url_for('posts.feed'))
        
        # Cria o post no banco de dados
        post_id = db.create_post(conteudo, categoria)
        
        flash('Seu desabafo foi enviado com sucesso!')
        return redirect(url_for('posts.feed'))
    
    return redirect(url_for('posts.feed'))

