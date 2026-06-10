import sqlite3

conn = sqlite3.connect("urls.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT,
    short_code TEXT,
    clicks INTEGER,
    user_id INTEGER
)
""")

conn.commit()
conn.close()