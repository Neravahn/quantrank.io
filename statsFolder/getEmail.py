import sqlite3

DB_PATH = 'database.db'

def emailOf(username):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT email FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    email = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return email