from database import get_db

def create_order(total):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (total) VALUES (?)",(total,))
    conn.commit()
    conn.close()