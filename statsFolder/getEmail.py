import sqlite3

DB_PATH = 'home/quantrank/Quantrank.io/database.db'

def emailOf(username):

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    query = "SELECT email FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    email = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return email