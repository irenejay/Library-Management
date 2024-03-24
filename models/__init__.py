

import sqlite3

CONN = sqlite3.connect('library.db')
CURSOR = CONN.cursor()

def create_tables():
    """Create database tables if they do not exist"""
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    """)
    CONN.commit()
create_tables()

def drop_tables():
    """Drop database tables"""
    CURSOR.execute("DROP TABLE IF EXISTS authors")
    CURSOR.execute("DROP TABLE IF EXISTS books")
    CONN.commit()
