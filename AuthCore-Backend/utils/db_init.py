from database import get_db

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE,
                   password TEXT
                   )
                   """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()