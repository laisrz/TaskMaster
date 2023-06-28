def filter_tasks(cursor, status):
    if status == "I":
        filter = "incomplete"
    elif filter == "C":
        filter = "complete"
    cursor.execute("SELECT * FROM tasks WHERE status = ?", [filter])
    data = cursor.fetchall()
