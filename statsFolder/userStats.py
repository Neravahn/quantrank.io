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


def update_stats(username, difficulty, topic):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    ALLOWED_COLUMNS = {
        "easy", "medium", "hard",
        "ratio_proportion", "indices", "logarithm",
        "equations", "inequalities", "finance",
        "permutations", "progression", "central_tendency",
        "dispersion", "correlation"
    }

    if difficulty not in ALLOWED_COLUMNS or topic not in ALLOWED_COLUMNS:
        raise ValueError("Invalid column name")

    query = f"""
    UPDATE stats
    SET 
        "{difficulty}" = "{difficulty}" + 1,
        "{topic}" = "{topic}" + 1
    WHERE username = ?
    """

    cursor.execute(query, (username,))
    conn.commit()
    cursor.close()
    conn.close()


def update_points(username, points):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if points > 0:
        query = "UPDATE stats SET total_points = total_points + 1 WHERE username = ?"
    elif points < 0:
        query = "UPDATE stats SET total_points = total_points - 1 WHERE username = ?"

    cursor.execute(query, (username,))
    conn.commit()
    cursor.close()
    conn.close()


def getChapterData(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    chapters = ["ratio_proportion", "indices", "logarithm",
        "equations", "inequalities", "finance",
        "permutations", "progression", "central_tendency",
        "dispersion", "correlation"]

    nos = []
    for i in range( len(chapters)):
        chapter = chapters[i]

        query = f"""SELECT "{chapter}" FROM stats where username = ?"""
        cursor.execute(query, (username,))

        data = cursor.fetchone()[0]

        nos.append(data)


    cursor.close()
    conn.close()
    return nos






