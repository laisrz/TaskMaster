import sqlite3


def main():

    # define connection and cursor

    db = sqlite3.connect('taskmaster.db')

    cursor = db.cursor()

    # create tasks table

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                        task_id INTEGER NOT NULL PRIMARY KEY,
                        description TEXT NOT NULL,
                        status TEXT NOT NULL
                      )""")

    # call menu

    option = menu()

    # create a task

    if option == "C":
        description = input("Type a new task: ")
        # create a list of accepted status for tasks
        status = input("Type new task status: ")
        # find out how to insert creation date from the system
        cursor.execute("INSERT INTO tasks (description, status) VALUES (?, ?)", (description, status))
        last_id = cursor.execute("SELECT last_insert_rowid()")
        cursor.execute("SELECT * FROM tasks WHERE task_id = ?", last_id)
        data = cursor.fetchone()
        for column in data:
            print(f"New task added: {column}")
        
        
        

    # close connection with database

    db.close()


def menu():
    # display the main menu

    option = input("Main menu\n \
    Press C to create a task;\n \
    Press V to view all tasks;\n \
    Press U to update a task status;\n \
    Press M to modify a task description;\n \
    Press D to delete a task;\n \
    Press E to exit the program;\n \
    Choose the option you want to run: ").upper()
    
    return option


main()
