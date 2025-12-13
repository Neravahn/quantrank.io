import sqlite3

DB_PATH = 'database.db'

def getUserData(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()


    query = "SELECT * FROM stats WHERE username = ?"
    cursor.execute(query, (username,))
    row = cursor.fetchall()[0]
    easy = row[1]
    medium = row[2]
    hard = row[3]
    total_points = row[4]

    return easy, medium, hard, total_points


