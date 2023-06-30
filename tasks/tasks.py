def filter_tasks(cursor, status):
    if status == "i":
        filter = "incomplete"
    elif status == "c":
        filter = "complete"
    cursor.execute("SELECT * FROM tasks WHERE status = ?", [filter])
    data = cursor.fetchall()
    return data

def menu():
    # display the main menu
    option = input("Main menu\n \
    Press C to create a task;\n \
    Press V to view tasks;\n \
    Press U to update a task status;\n \
    Press M to modify a task description;\n \
    Press D to delete a task;\n \
    Press E to exit the program;\n \
    Choose the option you want to run: ").lower()
    
    return option     

def prompt_task():
    # prompt the user for the new task
    return input("Type a new task: ")
    
    
def insert_task(cursor, conn, description):
    # insert task on database
    cursor.execute("INSERT INTO tasks (description, status, creation_date) VALUES (?, ?, ?)", (description, "incomplete", date.today()))
    conn.commit()
    

def print_new_task(description):
    # print task
    print("**********************************")
    print(f"New task sucessfully added:\nDescription: {description} Status: incomplete Creation date: {date.today()}")
    print("**********************************")

def select_all_tasks(cursor):
    # select and store data on a list (data)
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()


def print_tasks(data):
    # print tasks from database
    print("**********************************")
    print("Recorded tasks")
    for row in data:
        print(f"Id:{row[0]} Description:{row[1]} Status:{row[2]} Creation date:{row[3]}")
    print("**********************************")


def prompt_filter():
    # prompt user to choose whether to filter task or not
    return input("Press F to filter this task list or\n Press R to return to main menu: ").lower()

def prompt_status():
    # prompt user to choose which filter to use
    return input("Press I to filter the task list by incompleted tasks only or\nPress C to filter by completed tasks only: ").lower()
    

def filter_tasks(cursor, option, status):
    if option == "f":
        if status == "i":
            filter = "incomplete"
        elif status == "c":
            filter = "complete"
        cursor.execute("SELECT * FROM tasks WHERE status = ?", [filter])
        return cursor.fetchall()

    else:
        menu()


def prompt_id(cursor, command):
    # prompt the user for the id of the task to update
    while True:
        id = int(input(f"Please provide the id of the task you'd like to {command}: "))
        cursor.execute("SELECT task_id FROM tasks")
        rows = [r[0] for r in cursor]
        if id not in rows:
            print("Invalid id.")
        else:
            break
    return id

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

def prompt_delete(data):
    return input(f"Are you sure you want to delete\nId:{data[0]} Description:{data[1]} Status:{data[2]} Creation date:{data[3]}? Y/N: ").lower()

def delete_task(cursor, conn, confirmation, id):
    if confirmation == "y":
        cursor.execute("DELETE FROM tasks WHERE task_id = ?", [id])
        conn.commit()
    else:
        menu()

def print_sucess(command):
    print("**********************************")
    print(f"Task sucessfully {command}")
    print("**********************************")
 




if __name__ == '__main__':
    main()
