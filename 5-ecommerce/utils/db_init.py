from database import get_db

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price REAL
                )
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS cart(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    quantity INTEGER
                )
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   total REAL
                )
                """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()