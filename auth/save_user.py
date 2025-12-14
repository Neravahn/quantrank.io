import sqlite3
from mathhash import hash_password



DB_PATH = 'database.db'


def save(name, username, email, password, pfp):

    hashed = hash_password(password)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "INSERT INTO users (name, username, email, password, profile_pic) VALUES (?, ?, ?, ?)"

    cursor.execute(query, (name, username, email, hashed, pfp))

    conn.commit()
    cursor.close()
    conn.close()
