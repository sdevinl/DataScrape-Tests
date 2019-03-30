from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import re

url = "https://wikipedia.org/"
r = requests.get(url, params = dict(
    query='web scrapng'
))

print (r.status_code)

text = r.text

print(r.headers.get('content-type','unknown'))


soup = BeautifulSoup(r.text,'html.parser')

tags = soup.find_all("li", "search-result")

tags.text