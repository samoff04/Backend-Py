from database import get_db

def add_to_cart(product_id, quantity):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cart (product_id, quantity) VALUES (?, ?)", (product_id, quantity))
    conn.commit()
    conn.close()

def get_cart():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cart")
    rows = cursor.fetchall()
    conn.close()
    return rows