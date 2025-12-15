import sqlite3


DB_PATH = 'database.db'

def insert(chapter_name, difficulty, function_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "INSERT INTO question_metadata (chapter_name, difficulty, function_name) VALUES (?, ?, ?)"

    cursor.execute(query, (chapter_name, difficulty, function_name))
    conn.commit()
    cursor.close()
    conn.close()

    return 'done'

    




def index_exists(index_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1
        FROM sqlite_master
        WHERE type='index' AND name=?
    """, (index_name,))

    exists = cursor.fetchone() is not None
    conn.close()
    return exists


print(index_exists("idx_heatmap_user_date"))



