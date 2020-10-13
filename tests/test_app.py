from app import headlineGatherer, headlineStorer
import sqlite3
import pytest


@pytest.fixture
def database_setup():
    """ Fixture to set up the in-memory database with test data """
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    c.execute('''CREATE TABLE headlines (headline text)''')

    headline_sample = [
        ('Sample Headline #1'),
        ('Sample Headline #2')
    ]

    for item in headline_sample:
        c.execute("INSERT INTO headlines(headline) VALUES(?)", (item,))
    yield conn


def test_headlineGatherer():
    url = 'https://reuters.com'
    tag = 'h3'
    className = 'story-content'

    # Assert that headlineGatherer returns a list
    assert headlineGatherer(url, tag, className) == []


def test_connection(database_setup):
    c = database_setup

    assert len(list(c.execute('SELECT * FROM headlines'))) == 2


# def test_headlineStorer():
#     dbFilePath = pass
#     dfHeadline = pass
