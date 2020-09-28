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
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')

    srcRes = soup.find_all(tag)
    results = []
    for r in srcRes:
        results.append(r.get_text())

    return results
