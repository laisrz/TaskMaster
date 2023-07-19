import sqlite3
from datetime import date
from tasks import db_operations
from classes import task

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
        
        actions = {"c": task.create_task, "v": task.view_task, "f": task.filter_task, "u": task.update_status, "m": task.update_description, "d": task.delete, "e": exit}

        # create a task
        if option == "c":
            # prompt task from the user
            description = prompt_task()

            # call method create_task 
            actions["c"](description)

            # insert new task into database
            db_operations.insert_task(cursor, conn, description)
            print_new_task(description)

   
        # view tasks
        elif option == "v":
            # select and print all tasks
            data = actions["v"](cursor)
            print_tasks(data)

            #filter tasks
            #prompt the user to filter or return
            option_filter = prompt_filter()

            if option_filter == "f":
                # prompt the user for the new status
                status = prompt_status()

                # select data based on the status the user selected
                data = actions["f"](cursor, status)
                print_tasks(data)

            else:
                menu()
            
        
        # update task status
        elif option == "u":
            #view all tasks
            data = actions["v"](cursor)
            print_tasks(data)
            
            # prompt the user for the id of the task to update
            id = prompt_id(cursor, "update")

            # prompt the user for the new status and update database
            new_status = input("Type the new status: ")
            actions["u"](cursor, conn, new_status, id)

            # print success
            print_success("updated")
            
        
        # update task description
        elif option == "m":
            #view all tasks
            data = actions["v"](cursor)
            print_tasks(data)

            # prompt the user for the id of the task to update
            id = prompt_id(cursor, "update")

            # prompt the user for the new description and update database
            new_description = input("Type the new description: ")
            actions["m"](cursor, conn, new_description, id)
            
            # print success
            print_success("updated")
            

        # delete task
        elif option == "d":
            #view all tasks
            data = actions["v"](cursor)
            print_tasks(data)

            # prompt the user for the id of the task to update
            id = prompt_id(cursor, "delete")

            # select task
            data = db_operations.select_one_task(cursor, id)
            
            # print task to be deleted and prompt the user for confirmation
            confirm = prompt_delete(data)

            # delete task
            if confirm == "y":
                actions["d"](cursor, conn, id)
                print_success("deleted")
            else:
                menu()

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
    return input("Type a new task: ")
    
    
def print_new_task(description):
    # print task
    print("**********************************")
    print(f"New task sucessfully added:\nDescription: {description} Status: incomplete Creation date: {date.today()}")
    print("**********************************")


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


def prompt_delete(data):
    return input(f"Are you sure you want to delete\nId:{data[0]} Description:{data[1]} Status:{data[2]} Creation date:{data[3]}? Y/N: ").lower()


def print_success(command):
    print("**********************************")
    print(f"Task sucessfully {command}")
    print("**********************************")


if __name__ == '__main__':
    main()


