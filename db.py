import sqlite3

def database_connection():
    # define connection and cursor
    conn = sqlite3.connect('taskmaster.db')

    cursor = conn.cursor()

    return conn, cursor
    
def database_creation(cursor):
    # create tasks table
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                    task_id INTEGER NOT NULL PRIMARY KEY,
                    description TEXT NOT NULL,
                    status TEXT NOT NULL,
                    creation_date INTEGER NOT NULL
                    )""")
