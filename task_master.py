import sqlite3
from datetime import date


def main():

    # define connection and cursor

    conn = sqlite3.connect('taskmaster.db')

    cursor = conn.cursor()

    # create tasks table

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                        task_id INTEGER NOT NULL PRIMARY KEY,
                        description TEXT NOT NULL,
                        status TEXT NOT NULL,
                        creation_date INTEGER NOT NULL
                      )""")

    # call menu
    while True:
        option = menu()

        # create a task
        if option == "c":
            # prompt task from the user
            new_description, date = prompt_task()
            # insert task on database
            insert_task(cursor, conn, new_description, date)
            # print new task added
            print_new_task(new_description, date)


        # view tasks
        elif option == "v":
            # view all tasks
            data = view_tasks(cursor)
            print_tasks(data)
            
            # filter tasks
            option = prompt_filter()
            status = prompt_status()
            data = filter_tasks(cursor, option, status)
            print_tasks(data)
           

        # update task status
        elif option == "u":
            #view all tasks
            data = view_tasks(cursor)
            print_tasks(data)
            
            # prompt the user for the id of the task to update
            id = prompt_id(cursor, "update")

            # prompt the user for the new status and update database
            new_status = input("Type the new status: ")
            update_status(cursor, conn, new_status, id)

            # print success
            print_sucess("updated")
            
        
        # update task description
        elif option == "m":
            #view all tasks
            data = view_tasks(cursor)
            print_tasks(data)

            # prompt the user for the id of the task to update
            id = prompt_id(cursor, "update")

            # prompt the user for the new description and update database
            new_description = input("Type the new description: ")
            update_description(cursor, conn, new_description, id)

            # print success
            print_sucess("updated")
            

        # delete task
        elif option == "d":
            #view all tasks
            data = view_tasks(cursor)
            print_tasks(data)

            # prompt the user for the id of the task to update
            id = prompt_id(cursor, "delete")

            # select task
            data = select_task(cursor, id)
            
            # print task to be deleted and prompt the user for confirmation
            confirmation = confirm_deletion(data)
            # delete task
            delete_task(cursor, conn, confirmation, id)

            #print success
            print_sucess("deleted")

        # exit
        elif option == "e":
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
    Choose the option you want to run: ").lower()
    
    return option     

def prompt_task():
    # prompt the user for the new task
    description = input("Type a new task: ")
    # get the current date
    creation_date = date.today()
    return description, creation_date
    
    
def insert_task(cursor, conn, description, creation_date):
    # insert task on database
    cursor.execute("INSERT INTO tasks (description, status, creation_date) VALUES (?, ?, ?)", (description, "incomplete", creation_date))
    conn.commit()
    

def print_new_task(description, date):
    # print task
    print("**********************************")
    print(f"New task sucessfully added:\nDescription: {description} Status: incomplete Creation date: {date}")
    print("**********************************")

def view_tasks(cursor):
    # select and store data on a list (data)
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()
    return data

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

def select_task(cursor, id):
    cursor.execute("SELECT * FROM tasks WHERE task_id = ?", [id])
    return cursor.fetchone()

def confirm_deletion(data):
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
