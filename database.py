import sqlite3

def initialize_db():
    conn = sqlite3.connect('financier.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact TEXT,
        email TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        clientId INTEGER,
        amount REAL,
        interestRate REAL,
        startDate TEXT,
        endDate TEXT,
        FOREIGN KEY(clientId) REFERENCES clients(id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
