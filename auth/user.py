import sqlite3


DB_PATH = 'home/quantrank/QuantRank.io/database.db'

def check_username(username):

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    query = "SELECT name FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return user


def check_email(email):

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    query = "SELECT name FROM users WHERE email = ?"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return user

def getPFP(username):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("SELECT profile_pic FROM users WHERE username = ?", (username,))
    pfp = cursor.fetchone()[0]
    conn.close()
    

    return pfp