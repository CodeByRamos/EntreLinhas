import sqlite3
from datetime import datetime
import os

# Caminho do banco de dados
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'entrelinhas.db')

def get_db_connection():
    """Estabelece e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Para acessar colunas pelo nome
    return conn

def init_db():
    """Inicializa o banco de dados com as tabelas necessárias."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Tabela de posts (desabafos)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mensagem TEXT NOT NULL,
            data_postagem TEXT NOT NULL,
            categoria TEXT NOT NULL,
            visivel INTEGER DEFAULT 1
        )
    ''')
    
    # Tabela de comentários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            comment_text TEXT NOT NULL,
            data_comentario TEXT NOT NULL,
            visivel INTEGER DEFAULT 1,
            FOREIGN KEY (post_id) REFERENCES posts (id)
        )
    ''')
    
    # Tabela de reações
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            reaction_type TEXT NOT NULL,
            data_reacao TEXT NOT NULL,
            FOREIGN KEY (post_id) REFERENCES posts (id)
        )
    ''')
    
    # Tabela de contagem de reações (para performance)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reaction_counts (
            post_id INTEGER NOT NULL,
            reaction_type TEXT NOT NULL,
            count INTEGER DEFAULT 0,
            PRIMARY KEY (post_id, reaction_type),
            FOREIGN KEY (post_id) REFERENCES posts (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def get_posts(limit=50):
    """Retorna os posts mais recentes."""
    conn = get_db_connection()
    posts = conn.execute('''
        SELECT id, mensagem, categoria, data_postagem 
        FROM posts 
        WHERE visivel = 1 
        ORDER BY id DESC 
        LIMIT ?
    ''', (limit,)).fetchall()
    conn.close()
    return posts

def get_post(post_id):
    """Retorna um post específico pelo ID."""
    conn = get_db_connection()
    post = conn.execute('''
        SELECT id, mensagem, categoria, data_postagem 
        FROM posts 
        WHERE id = ? AND visivel = 1
    ''', (post_id,)).fetchone()
    conn.close()
    return post

def create_post(mensagem, categoria):
    """Cria um novo post."""
    conn = get_db_connection()
    data_postagem = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO posts (mensagem, categoria, data_postagem)
        VALUES (?, ?, ?)
    ''', (mensagem, categoria, data_postagem))
    
    post_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return post_id

def get_comments(post_id):
    """Retorna os comentários de um post específico."""
    conn = get_db_connection()
    comments = conn.execute('''
        SELECT id, comment_text, data_comentario 
        FROM comments 
        WHERE post_id = ? AND visivel = 1 
        ORDER BY id ASC
    ''', (post_id,)).fetchall()
    conn.close()
    return comments

def create_comment(post_id, comment_text):
    """Cria um novo comentário para um post."""
    conn = get_db_connection()
    data_comentario = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO comments (post_id, comment_text, data_comentario)
        VALUES (?, ?, ?)
    ''', (post_id, comment_text, data_comentario))
    
    comment_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return comment_id

def add_reaction(post_id, reaction_type):
    """Adiciona uma reação a um post e atualiza a contagem."""
    conn = get_db_connection()
    data_reacao = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    cursor = conn.cursor()
    # Registra a reação individual
    cursor.execute('''
        INSERT INTO reactions (post_id, reaction_type, data_reacao)
        VALUES (?, ?, ?)
    ''', (post_id, reaction_type, data_reacao))
    
    # Atualiza a contagem de reações
    cursor.execute('''
        INSERT INTO reaction_counts (post_id, reaction_type, count)
        VALUES (?, ?, 1)
        ON CONFLICT(post_id, reaction_type) DO UPDATE SET
        count = count + 1
    ''', (post_id, reaction_type))
    
    conn.commit()
    conn.close()

def get_reaction_counts(post_id):
    """Retorna a contagem de cada tipo de reação para um post."""
    conn = get_db_connection()
    reaction_counts = conn.execute('''
        SELECT reaction_type, count 
        FROM reaction_counts 
        WHERE post_id = ?
    ''', (post_id,)).fetchall()
    conn.close()
    
    # Converte para um dicionário para facilitar o uso
    counts = {}
    for row in reaction_counts:
        counts[row['reaction_type']] = row['count']
    
    return counts

# Inicializa o banco de dados se este arquivo for executado diretamente
if __name__ == "__main__":
    init_db()
    print("Banco de dados inicializado com sucesso!")

