import sqlite3
import questions.chapter0ne as ch1
import questions.chapterSix as ch6
import questions.chapterFour as ch4


DB_PATH = '/home/quuantrank/QuantRank.io/database.db'
def check(difficulty, chapter_name):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    cursor = conn.cursor()

    query = """
    SELECT function_name FROM question_metadata WHERE chapter_name = ? and difficulty = ? ORDER BY RANDOM() LIMIT 1
    """

    cursor.execute(query, (chapter_name, difficulty))
    func_name = cursor.fetchone()[0]
    if chapter_name == 'ratio_proportion':
        x = ch1
    if chapter_name == 'finance':
        x = ch6
    if chapter_name == 'equations':
        x = ch4
    
    func = getattr(x, func_name)
    question, options, answer = func()

    return question, options, answer




