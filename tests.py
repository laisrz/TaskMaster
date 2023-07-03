import sqlite3
import pytest
from tasks import tasks

@pytest.fixture
def session(): 
    connection = sqlite3.connect(':memory:')
    db_session = connection.cursor()
    yield db_session
    connection.close()


@pytest.fixture
def setup_db(session): 
    session.execute('''CREATE TABLE tasks (
                        task_id INTEGER NOT NULL PRIMARY KEY,
                        description TEXT NOT NULL,
                        status TEXT NOT NULL,
                        creation_date INTEGER NOT NULL)''')
    
    session.connection.commit()

@pytest.mark.usefixtures("setup_db")
def test_filter_incomplete_tasks(session):
    result = tasks.filter_tasks(session, "i")
    assert len(result) == 0
    
@pytest.mark.usefixtures("setup_db")
def test_filter_complete_tasks(session):
    result = tasks.filter_tasks(session, "c")
    assert len(result) == 0
