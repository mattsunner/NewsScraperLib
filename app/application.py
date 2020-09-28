"""
Reuters-Pipeline

Author: Matthew Sunner, 2020
"""

from bs4 import BeautifulSoup
import lxml
import requests

# class SiteParser(self, url):
#     self.url = url


def headlineGatherer(url, tag):
    """headlineGatherer: Function to return an array of headlines from a given URL and HTML tag.

    Args:
        url (str): URL for the site being used to gather headlines from.
        tag (str): HTML tag for attribute(s) being gathered (eg.. 'h1', 'h2')

    Returns:
        array: Result of the function is an array of headline text gathered from the URL provided.
    """
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')

    srcRes = soup.find_all(tag)
    results = []
    for r in srcRes:
        results.append(r.get_text())

    return results
