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

