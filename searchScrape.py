import requests
from bs4 import BeautifulSoup
import json

searchTerm = input("What book do you want to search for?")

url = 'https://www.goodreads.com/book/show/' + bookLink
response = requests.get(url, timeout=5)  
content = BeautifulSoup(response.content, "html.parser")