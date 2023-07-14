import sqlite3
from datetime import date
from tasks import tasks
from classes import options

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
        option = options.Option(option) #create object option

        # create a task
        if option.is_create_task():
            # prompt task from the user
            new_description = prompt_task()
            # insert task on database
            tasks.insert_task(cursor, conn, new_description)
            # print new task added
            print_new_task(new_description)


        # view tasks
        elif option.is_view_tasks():
            # select and print all tasks
            data = tasks.select_all_tasks(cursor)
            print_tasks(data)
            
            # filter tasks
            #prompt the user to filter or return
            option_filter = options.Option(prompt_filter()) #create object

            # select data based on the status the user selected
            if option_filter.is_filter():
                #prompt the user to choose with filter to use
                status = prompt_status()
                data = tasks.filter_tasks(cursor, status)
                print_tasks(data)
            else:
                menu()
            

        # update task status
        elif option.is_update():
            #view all tasks
            data = tasks.select_all_tasks(cursor)
            print_tasks(data)
            
            # prompt the user for the id of the task to update
            id = prompt_id(cursor, "update")

            # prompt the user for the new status and update database
            new_status = input("Type the new status: ")
            tasks.update_status(cursor, conn, new_status, id)

            # print success
            print_success("updated")
            
        
        # update task description
        elif option.is_modify():
            #view all tasks
            data = tasks.select_all_tasks(cursor)
            print_tasks(data)

            # prompt the user for the id of the task to update
            id = prompt_id(cursor, "update")

            # prompt the user for the new description and update database
            new_description = input("Type the new description: ")
            tasks.update_description(cursor, conn, new_description, id)

            # print success
            print_success("updated")
            

        # delete task
        elif option.is_delete():
            #view all tasks
            data = tasks.select_all_tasks(cursor)
            print_tasks(data)

            # prompt the user for the id of the task to update
            id = prompt_id(cursor, "delete")

            # select task
            data = tasks.select_one_task(cursor, id)
            
            # print task to be deleted and prompt the user for confirmation
            confirm = prompt_delete(data)
            option = options.Option(confirm) #create object

            # delete task
            if option.is_confirm_delete():
                tasks.delete_task(cursor, conn, id)
                print_success("deleted")
            else:
                menu()

        # exit
        elif option.is_exit():
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


