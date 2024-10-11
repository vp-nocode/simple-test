import pytest
from main_db import init_db, add_user, get_user


@pytest.fixture
def db_conn():
   conn = init_db()
   yield conn
   conn.close()

def test_add_or_get_user(db_conn):
    add_user(db_conn, "Sasha", 30)
    user = get_user(db_conn, "Sasha")
    assert user == (1, "Sasha", 30)

def test_add3_or_get_user(db_conn):
    add_user(db_conn, "Sasha", 30)
    add_user(db_conn, "Bob", 25)
    add_user(db_conn, "Den", 22)
    user = get_user(db_conn, "Bob")
    assert user == (2, "Bob", 25)
