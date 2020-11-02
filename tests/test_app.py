from app import headlineGatherer, headlineStorer, show_all_records, show_records, add_to_mysql
import os
import os.path
from os import path
from os.path import dirname, join
from dotenv import load_dotenv, find_dotenv
import sqlite3
import pytest
import mysql.connector

sample_headlines = [
    ('Sample Headline #1'),
    ('Sample Headline #2')
]


@pytest.fixture
def database_setup():
    """ Fixture to set up the in-memory database with test data """

    if path.exists('testing.db') == True:
        conn = sqlite3.connect('testing.db')
        yield conn
    else:
        conn = sqlite3.connect('testing.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE headlines (headline text)''')

        for item in sample_headlines:
            c.execute("INSERT INTO headlines(headline) VALUES(?)", (item,))

        conn.commit()

        yield conn


def test_connection(database_setup):
    c = database_setup

    assert len(list(c.execute('SELECT * FROM headlines'))) == 2


def test_headlineGatherer():
    url = 'https://reuters.com'
    tag = 'h3'
    className = 'story-content'

    # Assert that headlineGatherer returns a list
    assert headlineGatherer(url, tag, className) == []


def test_headlineStorer():

    headline_addition = ('Sample Headline #3', 'Sample Headline #4')

    headlineStorer('file::memory:?cache=shared', headline_addition)

    conn = sqlite3.connect('file::memory:?cache=shared')
    cur = conn.cursor()
    cur.execute("SELECT * FROM headlines")
    rows = cur.fetchall()

    os.remove('file::memory:?cache=shared')

    assert len(rows) == 2


def test_show_all_records():

    s = show_all_records('testing.db')

    assert len(s) == 2


def test_show_records():

    s = show_records('testing.db', '#1')

    assert len(s) == 1


def test_add_to_mysql():
    load_dotenv()
    DATABASE_PASSWORD = os.environ.get("TESTING_DB_PW")

    # Test Variables
    host = 'Matthews-MacBook-Pro.local'
    user = 'root'
    password = DATABASE_PASSWORD
    database = 'lib_test_testing'
    values = ['headline #1', 'headline #2']

    print(password)

    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Test the function
    add_to_mysql(host, user, password, database, values)

    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM headlines")

    myresult = mycursor.fetchall()

    mycursor.execute("DELETE FROM headlines")

    db.commit()

    mycursor.close()

    assert len(myresult) == len(values)
