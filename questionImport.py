import sqlite3
import questions.chapter0ne as ch1


DB_PATH = 'database.db'
def check(difficulty, chapter_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT function_name FROM question_metadata WHERE chapter_name = ? and difficulty = ? ORDER BY RANDOM() LIMIT 1
    """

    cursor.execute(query, (chapter_name, difficulty))
    func_name = cursor.fetchone()[0]

    return func_name

func_name = check('easy', 'ratio_proportion')
func = getattr(ch1, func_name)
q, o, a = func()
print(q, o, a)

