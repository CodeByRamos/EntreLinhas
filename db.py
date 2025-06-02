import sqlite3

def init_db():
    conn = sqlite3.connect('EntreLinhas.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mensagem TEXT NOT NULL,
            data_postagem DATETIME NOT NULL,
            categoria TEXT,
            reacoes INTEGER DEFAULT 0,
            visivel BOOLEAN DEFAULT 1
        )
    ''')

    conn.commit()
    conn.close()
