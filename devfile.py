import random
from datetime import datetime, timedelta
import sqlite3
from zoneinfo import ZoneInfo

DB_PATH = 'database.db'

def create_test_heatmap_data(username="prashant", rows=8, cols=50):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    today = datetime.now(ZoneInfo("Asia/Kolkata")).date()
    total_days = rows * cols

    # Insert from oldest to newest so bottom-right is latest
    for i in range(total_days):
        activity_date = today - timedelta(days=(total_days - 1 - i))  # decrement properly
        points = random.randint(0, 20)
        cursor.execute("""
            INSERT INTO heatmap (username, activity_date, points)
            VALUES (?, ?, ?)
            ON CONFLICT(username, activity_date) DO UPDATE SET points=excluded.points
        """, (username, activity_date.isoformat(), points))

    conn.commit()
    conn.close()
    print(f"Inserted/updated {total_days} rows for {username}.")

# Run this once
#create_test_heatmap_data()
