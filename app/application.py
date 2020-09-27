"""
Reuters-Pipeline

Author: Matthew Sunner, 2020
"""

from bs4 import BeautifulSoup
import lxml
import requests

# class SiteParser(self, url):
#     self.url = url

url = 'https://www.reuters.com/'
response = requests.get(url)
html_doc = response.text
soup = BeautifulSoup(html_doc, 'lxml')

print(soup)
