from database import get_db

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()