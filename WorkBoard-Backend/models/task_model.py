from database import get_db

def create_task(title, description, priority, user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, description, status, priority, user_id)
        VALUES (?, ?, ?, ?)
    """, (title, description, "pending", priority, user_id))
    conn.commit()
    conn.close()

def get_tasks(user_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id))
    tasks = cursor.fetchall()
    conn.close()
    return tasks