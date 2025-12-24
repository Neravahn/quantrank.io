import sqlite3
from mathhash import hash_password



DB_PATH = '/home/quantrank/QuantRank.io/database.db'


def save(name, username, email, password, pfp):

    hashed = hash_password(password)

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    query = "INSERT INTO users (name, username, email, password, profile_pic) VALUES (?, ?, ?, ?)"

    cursor.execute(query, (name, username, email, hashed, pfp))

    conn.commit()
    cursor.close()
    conn.close()
