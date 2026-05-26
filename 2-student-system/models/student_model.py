from database import get_db

def add_student(name, age, course):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_student(id, name, age, course):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET name=?, age=?, course=?
        WHERE id=?
    """, (name, age, course, id))
    conn.commit()
    conn.close()

def delete_student(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id))
    conn.commit()
    conn.close()