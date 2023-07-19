from datetime import date

def insert_task(cursor, conn, description):
    # insert task on database
    cursor.execute("INSERT INTO tasks (description, status, creation_date) VALUES (?, ?, ?)", (description, "incomplete", date.today()))
    conn.commit()

def select_all_tasks(cursor):
    # select and store data on a list (data)
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def filter_tasks(cursor, status):
    if status == "i":
        filter = "incomplete"
    elif status == "c":
        filter = "complete"
    cursor.execute("SELECT * FROM tasks WHERE status = ?", [filter])
    return cursor.fetchall()

def update_status(cursor, conn, new_status, id):
    #update status of task
    cursor.execute("UPDATE tasks SET status = ? WHERE task_id = ?", (new_status, id))
    conn.commit()

def update_description(cursor, conn, new_description, id):
    cursor.execute("UPDATE tasks SET description = ? WHERE task_id = ?", (new_description, id))
    conn.commit()

def select_one_task(cursor, id):
    cursor.execute("SELECT * FROM tasks WHERE task_id = ?", [id])
    return cursor.fetchone()
    
def delete_task(cursor, conn, id):
    cursor.execute("DELETE FROM tasks WHERE task_id = ?", [id])
    conn.commit()

