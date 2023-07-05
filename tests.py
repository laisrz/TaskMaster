import sqlite3
import pytest
from tasks import tasks as t
from datetime import date

# for tests that require a cursor
@pytest.fixture
def session(): 
    connection = sqlite3.connect(':memory:')
    db_session = connection.cursor()
    yield db_session
    connection.close()

# for tests that require a connection
@pytest.fixture
def connection(): 
    connection = sqlite3.connect(':memory:')
    yield connection
    connection.close()



@pytest.fixture
def setup_db(session): 
    session.execute('''CREATE TABLE tasks (
                        task_id INTEGER NOT NULL PRIMARY KEY,
                        description TEXT NOT NULL,
                        status TEXT NOT NULL,
                        creation_date INTEGER NOT NULL)''')
    
    session.execute('''INSERT INTO tasks (description, status, creation_date)
                         VALUES ("Example task", "incomplete", 2023-06-30),
                         ("Example task 1", "incomplete", 2023-07-01),
                         ("Example task 2", "complete", 2023-07-02)''')
    yield session.connection.commit()

    


@pytest.mark.usefixtures("setup_db")
def test_select_all(session):
    result = t.select_all_tasks(session)

    assert len(result) == 3
    assert result[0][1] == "Example task"
    assert result[0][2] == "incomplete"
    assert result[0][3] == 2023-6-30

@pytest.mark.usefixtures("setup_db")
def test_filter_complete_tasks(session):
    result = t.filter_tasks(session, "c")

    assert len(result) == 1
    assert result[0][2] == "complete"

@pytest.mark.usefixtures("setup_db")
def test_filter_incomplete_tasks(session):
    result = t.filter_tasks(session, "i")

    assert len(result) == 2
    assert result[0][2] == "incomplete"


@pytest.mark.usefixtures("setup_db", "connection")
def test_update_status(session, connection):
    t.update_status(session, connection, "complete", 1)
    session.execute("SELECT * FROM tasks")
    result = session.fetchall()

    assert len(result) == 3
    assert result[0][2] == "complete"

@pytest.mark.usefixtures("setup_db", "connection")
def test_update_description(session, connection):
    t.update_description(session, connection, "new_description", 3)
    session.execute("SELECT * FROM tasks")
    result = session.fetchall()
    
    assert len(result) == 3
    assert result[2][1] == "new_description"

@pytest.mark.usefixtures("setup_db")
def test_select_one_task(session):
    result = t.select_one_task(session, 2)

    assert result[1] == "Example task 1"
    assert result[2] == "incomplete"
    assert result[3] == 2023-7-1

@pytest.mark.usefixtures("setup_db", "connection")
def test_delete_task(session, connection):
    t.delete_task(session, connection, 3)
    session.execute("SELECT * FROM tasks")
    result = session.fetchall()
    
    assert len(result) == 2
    assert result[0][1] == "Example task"
    assert result[0][2] == "incomplete"
    assert result[0][3] == 2023-6-30
        

@pytest.mark.usefixtures("setup_db", "connection")
def test_insert_task(session, connection):
    t.insert_task(session, connection, "Example 3")
    session.execute("SELECT * FROM tasks")
    result = session.fetchall()
    
    assert len(result) == 4
    assert result[3][1] == "Example 3"
    assert result[3][2] == "incomplete"
    assert result[3][3] == str(date.today())







    
