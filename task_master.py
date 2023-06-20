import sqlite3


def main():

    # define connection and cursor (deveria usar o try block?????)

    conn = sqlite3.connect('taskmaster.db')

    cursor = conn.cursor()

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
        description, status = create_task()
        # find out how to insert creation date from the system
        # deveria usar o try block aqui tb???
        cursor.execute("INSERT INTO tasks (description, status) VALUES (?, ?)", (description, status))
        conn.commit()
        last_id = cursor.lastrowid
        cursor.execute("SELECT * FROM tasks WHERE task_id = ?", [last_id])
        data = cursor.fetchone()
        print("**********************************")
        print(f"New task sucessfully added:\nId: {data[0]} Description: {data[1]} Status: {data[2]}")
        

        

        

        

        
        
        

    # close connection with database
    conn.close()
    # close cursor



def menu():
    # display the main menu
    option = input("Main menu\n\
    Press C to create a task;\n \
    Press V to view tasks;\n \
    Press U to update a task status;\n \
    Press M to modify a task description;\n \
    Press D to delete a task;\n \
    Press E to exit the program;\n \
    Choose the option you want to run: ").upper()
    
    return option

def create_task():

    description = input("Type a new task: ")
    # TODO: create a list of accepted status for tasks
    status = input("Type new task status: ")

    return description, status
        

if __name__ == '__main__':
    main()
