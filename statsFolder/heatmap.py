from datetime import datetime
import sqlite3
from zoneinfo import ZoneInfo



DB_PATH = '/home/prashant/Desktop/QuantRank.io/database.db'
def get_today_ist():
    return datetime.now(ZoneInfo("Asia/Kolkata")).date().isoformat()


def init_newUser(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today = get_today_ist()


    query = "INSERT INTO heatmap (username, activity_date, points) VALUES (?, ?, 0) ON CONFLICT (username, activity_date) DO NOTHING"
    cursor.execute(query, (username, today))
    conn.commit()
    cursor.close()
    conn.close()



def daily_Users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    today = get_today_ist()

    query = "SELECT username FROM users"
    cursor.execute(query)
    column = cursor.fetchall()

    for i in range(len(column)):
        username = column[i][0]
        query_2 = 'INSERT INTO heatmap (username, activity_date, points) VALUES (?, ?, 0) ON CONFLICT (username, activity_date) DO NOTHING'
        cursor.execute(query_2, (username, today))


    conn.commit()
    conn.close()




def save_Points(username, correct):
    today = get_today_ist()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()


    if correct == True:
        query = f""" 
        INSERT INTO heatmap (username, activity_date, points, total_attempted, total_correct)
        VALUES (?, ?, 1, 1, 1)
        ON CONFLICT(username, activity_date)
        DO UPDATE SET points = points + 1, total_attempted = total_attempted + 1, total_correct = total_correct + 1;
        """

    else:
        query = f""" 
        INSERT INTO heatmap (username, activity_date, points, total_attempted, total_correct)
        VALUES (?, ?, 0, 1, 0)
        ON CONFLICT(username, activity_date)
        DO UPDATE SET points = points + 0, total_attempted = total_attempted + 1, total_correct = total_correct + 0;
        """

    cursor.execute(query, (username, today))

    conn.commit()
    conn.close()



def getHeatMap_data(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT activity_date, points FROM heatmap WHERE username = ?"
    cursor.execute(query, (username,))
    data = cursor.fetchall()

    conn.close()

    return data

