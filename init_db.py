import sqlite3

DB_NAME = "entrelinhas.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mensagem TEXT NOT NULL,
            data_postagem TEXT NOT NULL,
            categoria TEXT,
            reacoes INTEGER DEFAULT 0,
            visivel INTEGER DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Banco criado com sucesso!")
