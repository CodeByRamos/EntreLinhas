<<<<<<< HEAD
from flask import Flask
import database as db
from routes.main import main
from routes.posts import posts
from routes.comments import comments
from routes.reactions import reactions

def create_app():
    """Função de fábrica para criar a aplicação Flask."""
    app = Flask(__name__)
    
    # Carrega configurações
    app.config.from_pyfile('config.py')
    
    # Inicializa o banco de dados
    db.init_db()
    
    # Registra os blueprints
    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(comments)
    app.register_blueprint(reactions)
    
    return app

# Cria a aplicação
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

=======
from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'chave-secreta-segura'  # Pode ser qualquer coisa segura.

# Banco de dados
def init_db():
    conn = sqlite3.connect('entrelinhas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mensagem TEXT NOT NULL,
            categoria TEXT NOT NULL,
            data_postagem TEXT NOT NULL,
            visivel INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    conn = sqlite3.connect('entrelinhas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT mensagem, categoria, data_postagem FROM posts WHERE visivel=1 ORDER BY data_postagem DESC")
    desabafos = cursor.fetchall()
    conn.close()
    return render_template('feed.html', desabafos=desabafos)

@app.route('/enviar', methods=['POST'])
def enviar():
    conteudo = request.form['conteudo']
    categoria = request.form['categoria']
    data_postagem = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('entrelinhas.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (mensagem, categoria, data_postagem) VALUES (?, ?, ?)',
                   (conteudo, categoria, data_postagem))
    conn.commit()
    conn.close()

    flash('Seu desabafo foi enviado com sucesso. Obrigado por compartilhar.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
>>>>>>> 7220671ada9990da703e916a48699f61aa59dd1f
