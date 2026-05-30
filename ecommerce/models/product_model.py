from database import get_db

def add_product(name, price):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)",(name, price))
    conn.commit()
    conn.close()

def get_products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    row = cursor.fetchall()
    conn.close()
    return rows