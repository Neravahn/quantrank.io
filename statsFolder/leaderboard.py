import sqlite3


DB_PATH = 'database.db'
def leaderboard_get():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """SELECT username, total_points
    FROM stats
    ORDER BY total_points DESC"""

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def rank(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()



