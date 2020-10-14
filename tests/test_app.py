from app import headlineGatherer, headlineStorer, show_all_records, show_records
import os
import os.path
from os import path
import sqlite3
import pytest

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
