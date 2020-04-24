from bs4 import BeautifulSoup
import requests
import re

html_page = requests.get("https://arstechnica.com")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print (link.get('href'))

#It downloads the raw html code with the line:


html_page = requests.get("https://arstechnica.com")

#A BeautifulSoup object is created and we use this object to find all links: