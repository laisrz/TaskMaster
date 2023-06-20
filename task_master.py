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
    while True:
        option = menu()

        # create a task
        if option == "C":
            # prompt the user for the new task
            description = input("Type a new task: ")
            # find out how to insert creation date from the system
            # deveria usar o try block aqui tb???
            cursor.execute("INSERT INTO tasks (description, status) VALUES (?, ?)", (description, "incomplete"))
            conn.commit()
            # retrieve id of last inserted task and select from database
            last_id = cursor.lastrowid
            cursor.execute("SELECT * FROM tasks WHERE task_id = ?", [last_id])
            data = cursor.fetchone()
            # print new task added
            print("**********************************")
            print(f"New task sucessfully added:\nId:{data[0]} Description:{data[1]} Status:{data[2]}")
            print("**********************************")

        # view tasks
        elif option == "V":
            # view all tasks
            view_tasks(cursor)
            
            # filter tasks
            filter_tasks(cursor)
           

        # update task status
        elif option == "U":
            #view all tasks
            view_tasks(cursor)
            
            # prompt the user for the id of the task to update
            update = "update"
            id = prompt_id(cursor, update)

            # prompt the user for the new status and update database
            new_status = input("Type the new status: ")
            cursor.execute("UPDATE tasks SET status = ? WHERE task_id = ?", (new_status, id))
            conn.commit()
            
        
        # update task description
        elif option == "M":
            #view all tasks
            view_tasks(cursor)

            # prompt the user for the id of the task to update
            update = "update"
            id = prompt_id(cursor, update)

            # prompt the user for the new description and update database
            new_description = input("Type the new description: ")
            cursor.execute("UPDATE tasks SET description = ? WHERE task_id = ?", (new_description, id))
            conn.commit()

        # delete task
        elif option == "D":
            #view all tasks
            view_tasks(cursor)

            # prompt the user for the id of the task to update
            delete = "delete"
            id = prompt_id(cursor, delete)

            # select task
            cursor.execute("SELECT * FROM tasks WHERE task_id = ?", [id])
            data = cursor.fetchone()
            
            # print task to be deleted and prompt the user for confirmation
            confirm_delete(cursor, conn, data, id)

        # exit
        elif option == "E":
            break

  
    
       
        
        

    # close connection with database
    conn.close()
 



def menu():
    # display the main menu
    option = input("Main menu\n \
    Press C to create a task;\n \
    Press V to view tasks;\n \
    Press U to update a task status;\n \
    Press M to modify a task description;\n \
    Press D to delete a task;\n \
    Press E to exit the program;\n \
    Choose the option you want to run: ").upper()
    
    return option     

def view_tasks(cursor):
    #select and display all tasks
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()
    print("**********************************")
    print("Recorded tasks")
    for row in data:
        print(f"Id:{row[0]} Description:{row[1]} Status:{row[2]}")

def filter_tasks(cursor):
    option = input("Press F to filter this task list or\n Press R to return to main menu: ").upper()
    if option == "F":
        print("**************************")
        filter = input("Press I to filter the task list by incompleted tasks only or\nPress C to filter by completed tasks only: ").upper()
        if filter == "I":
            filter = "incomplete"
        elif filter == "C":
            filter = "complete"
        cursor.execute("SELECT * FROM tasks WHERE status = ?", [filter])
        data = cursor.fetchall()
        print("**********************************")
        print("Recorded tasks")
        for row in data:
            print(f"Id:{row[0]} Description:{row[1]} Status:{row[2]}")
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

def confirm_delete(cursor, conn, data, id):
    print("**********************************")
    confirmation = input(f"Are you sure you want to delete\nId:{data[0]} Description:{data[1]} Status:{data[2]}? Y/N: ").upper()
    if confirmation == "Y":
        cursor.execute("DELETE FROM tasks WHERE task_id = ?", [id])
        conn.commit()
        print("Task sucessfully deleted")
    else:
        menu()
    
 




if __name__ == '__main__':
    main()
