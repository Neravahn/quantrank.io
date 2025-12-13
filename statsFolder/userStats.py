import sqlite3 


DB_PATH = 'database.db'

def stats_save(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = "INSERT INTO stats (username) VALUES (?)"
    cursor.execute(query, (username,))
    conn.commit()
    cursor.close()
    conn.close()


def update_stats(username, difficulty):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = None
    if difficulty == 'easy':
        query = "UPDATE stats SET easy = easy + 1 WHERE username = ?"
    elif difficulty == 'medium':
        query = "UPDATE stats SET medium = medium + 1 WHERE username = ?"
    elif difficulty == 'hard':
        query = "UPDATE stats SET hard = hard + 1 WHERE username = ?"


    cursor.execute(query, (username,))
    conn.commit()
    cursor.close()
    conn.close()


def update_points(username, points):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if points > 0:
        query = "UPDATE stats SET total_points = total_points + 1 WHERE username = ?"
    else:
        query = "UPDATE stats SET total_points = total_points - 1 WHERE username = ?"

    cursor.execute(query, (username,))
    conn.commit()
    cursor.close()
    conn.close()



update_stats('prashant', 'easy')
update_points('prashant', -1)
