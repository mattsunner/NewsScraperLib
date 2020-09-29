"""
Reuters-Pipeline

Author: Matthew Sunner, 2020
"""

from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
import os.path
from os import path
import sqlite3


def headlineGatherer(url, tag, className):
    """headlineGatherer: Function to return an array of headlines from a given URL and HTML tag.

    Args:
        url (str): URL for the site being used to gather headlines from.
        tag (str): HTML tag for attribute(s) being gathered (eg.. 'h1', 'h2').
        className (str): CSS Selector class for attribute(s) being gathered. Should be a subset of the provided tag.

    Returns:
        DataFrame: Result of the function is an Pandas DataFrame of headline text gathered from the URL provided.
    """
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')

    srcRes = soup.find_all(tag, {'class': className})
    resultsDf = pd.DataFrame(columns=['headline'])
    for r in srcRes:
        resultsDf = resultsDf.append({'headline': r}, ignore_index=True)

    return resultsDf


def headlineStorer(filePath):
    pass
