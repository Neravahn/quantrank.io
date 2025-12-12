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

    


insert('ratio_proportion', 'easy', 'proportion_8')
