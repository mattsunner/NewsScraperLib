"""
NewsScraperLib

Author: Matthew Sunner, 2020
"""

from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
import os.path
from os import path
import sqlite3
# MySQL connection requirement (to_mysql())
import mysql.connector


def headlineGatherer(url, tag, className):
    """headlineGatherer: Function to return an array of headlines from a given URL and HTML tag.

    Args:
        url (str): URL for the site being used to gather headlines from.
        tag (str): HTML tag for attribute(s) being gathered (eg.. 'h1', 'h2').
        className (str): CSS Selector class for attribute(s) being gathered. Should be a subset of the provided tag.

    Returns:
        List: Result of the function is an list of headline text gathered from the URL provided.
    """
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')

    srcRes = soup.find_all(tag, {'class': className})

    results = []
    for r in srcRes:
        results.append((str(r.get_text())))

    return results


def headlineStorer(dbFilePath, dfHeadline):
    """headlineStorer: Method to create/add headline list data into a SQLite3 database in the local filesystem.

    Args:
        dbFilePath (str): New or Existing name for the local database to be generated.
        dfHeadline (obj): List object of headlines, ex.. output from headlineGatherer method.
    """
    if path.exists(dbFilePath) == True:
        conn = sqlite3.connect(dbFilePath)
        c = conn.cursor()

        for item in dfHeadline:
            c.execute("INSERT INTO headlines(headline) VALUES(?)", (item,))

        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect(dbFilePath)
        c = conn.cursor()
        c.execute('''CREATE TABLE headlines (headline text)''')

        for item in dfHeadline:
            c.execute("INSERT INTO headlines(headline) VALUES(?)", (item,))

        conn.commit()
        conn.close()


def show_records(dbFilePath, selection):
    conn = sqlite3.connect(dbFilePath)
    c = conn.cursor()

    c.execute("SELECT * FROM headlines WHERE headline LIKE '%'||?||'%'",
              (selection,))

    rows = c.fetchall()
    return rows


def show_all_records(dbFilePath):
    conn = sqlite3.connect(dbFilePath)
    c = conn.cursor()

    c.execute("SELECT * FROM headlines")

    rows = c.fetchall()
    return rows


def add_to_mysql(host, user, password, database, values):
    """add_to_mysql: Method to add headlines to MySQL database. This method does not create schemas or databases on the MySQL server.

    Args:
        host (str): Host name of MySQL server
        user (str): Username used on MySQL server
        password (str): Password used on MySQL server
        database (str): Database name
        values (list): Python list of content to add to the database
    """
    try:
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        mycursor = db.cursor()
        add_values = values
        for value in add_values:
            sql = "INSERT INTO headlines (headline) VALUES (%s)"

            val = value

            mycursor.execute(sql, (val,))

        db.commit()

    except ValueError as e:
        print(e)

    finally:
        db.close()
