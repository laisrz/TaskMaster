import sqlite3
from tasks import tasks


def test_filter_incomplete_tasks():
    conn = sqlite3.connect('taskmaster.db')

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                        task_id INTEGER NOT NULL PRIMARY KEY,
                        description TEXT NOT NULL,
                        status TEXT NOT NULL,
                        creation_date INTEGER NOT NULL
                      )""")

    result = tasks.filter_tasks(cursor, "C")
    assert len(result) == 1

def test_filter_complete_tasks():
    pass
