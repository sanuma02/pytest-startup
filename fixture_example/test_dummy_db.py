from dummy_db import DummyDB
import pytest

'''
Example without using fixture, the methods setup_module and teardown_module are called at the beginning and at the end

cur = None
conn = None

def setup_module(module):
    global conn
    global cur
    db = DummyDB()
    conn = db.connect('some_server')
    cur = conn.cursor()

def teardown_module(module):
    cur.close()
    conn.close()

def test_johns_id():
    id = cur.execute("get_John")
    assert id == 123

def test_toms_id():
    id = cur.execute("get_Tom")
    assert id == 789
'''
#Example with Fixture global var do not have to be defined 

@pytest.fixture(scope="module")
def cur():
    print("setting up")
    db = DummyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close()
    conn.close()
    print("closing DB")

def test_johns_id(cur):
    id = cur.execute("get_John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute("get_Tom")
    assert id == 789