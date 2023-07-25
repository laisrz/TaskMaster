from tasks import db_operations

class Task:
    def __init__(self, description):
        self.description = description
        
    
    def create_task(description):
        return Task(description)


    def view_task(cursor):
        return db_operations.select_all_tasks(cursor)


    def filter_task(cursor, status):
        return db_operations.filter_tasks(cursor, status)


    def update_status(cursor, conn, status, id):
        return db_operations.update_status(cursor, conn, status, id)


    def update_description(cursor, conn, new_description, id):
        return db_operations.update_description(cursor, conn, new_description, id)

    def delete(cursor, conn, id):
        return db_operations.delete_task(cursor, conn, id)