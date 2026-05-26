from database import get_db

def create_post(title, content):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",(title, content))
    conn.commit()
    conn.close()

def get_posts():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_post(id, title, content):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE posts
        SET title=?, content=?
        WHERE id=?
    """, (title, content, id))
    conn.commit()
    conn.close()

def delete_post(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM posts WHERE id=?", (id,))
    conn.commit()
    conn.close()