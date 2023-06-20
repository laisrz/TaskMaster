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
            cursor.execute("SELECT * FROM tasks")
            data = cursor.fetchall()
            print("**********************************")
            print("Recorded tasks")
            for row in data:
                print(f"Id:{row[0]} Description:{row[1]} Status:{row[2]}")
            
            # filter tasks
            option2 = input("Press F to filter this task list or\n Press E to exit: ").upper()
            if option2 == "F":
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
                break

        # update task status
        elif option == "U":
            cursor.execute("SELECT * FROM tasks")
            data = cursor.fetchall()
            print("**********************************")
            print("Recorded tasks")
            for row in data:
                print(f"Id:{row[0]} Description:{row[1]} Status:{row[2]}")
            # prompt the user for the id of the task to update
            while True:
                id = int(input("Please provide the id of the task you'd like to update: "))
                cursor.execute("SELECT task_id FROM tasks")
                rows = [r[0] for r in cursor]
                if id not in rows:
                    print("Invalid id.")
                else:
                    break
            # prompt the user for the new status and update on database
            new_status = input("Type the new status of the task: ")
            cursor.execute("UPDATE tasks SET status = ? WHERE task_id = ?", (new_status, id))
            conn.commit()
        
        # update task description

        # delete task

        # exit
        else:
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


if __name__ == '__main__':
    main()
