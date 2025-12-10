import sqlite3


DB_PATH = 'database.db'

def check_username(username):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT name FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return user


def check_email(email):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT name FROM users WHERE email = ?"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return user