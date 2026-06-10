from database import get_db

def save_url(original_url, short_code, user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO urls (original_url, short_code, clicks, user_id)
        VALUES (?, ?, 0, ?)
    """, (original_url, short_code, user_id))
    conn.commit()
    conn.close()

def get_url(short_code):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM urls WHERE short_code=?", (short_code,))
    data = cursor.fetchone()
    conn.close()
    return data

def increase_clicks(short_code):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE urls SET clicks = clicks + 1
        WHERE short_code=?
    """, (short_code,))
    conn.commit()
    conn.close()