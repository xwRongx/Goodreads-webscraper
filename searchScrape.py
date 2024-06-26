import requests
from bs4 import BeautifulSoup
import json
import re
#imports libraries

searchTerm = input("What book do you want to search for?")
#asks user to enter a book name

url = 'https://www.goodreads.com/search?q=' + searchTerm
response = requests.get(url, timeout=5)  
content = BeautifulSoup(response.content, "html.parser")
#setup: url is the url searchbar takes you to

entryLink = []

for link in contentsearch.findAll('a', attrs={"class": "bookTitle"}, limit=5):
    entryLink.append('www.goodreads.com' + link.get('href'))
#takes the first 5 links on the page with the class bookTitle
#adds the goodreads url to the link path and appends it to the entryLink list 

linkArr = []

for tr in contentsearch.findAll('tr', attrs={"itemscope itemtype": "http://schema.org/Book"}, limit=5):
    linkObject = {
        "title": contentsearch.find("span", attrs={"role": "heading"}).text,
        "author": contentsearch.find("span", attrs={"itemprop":"name"}).text
    }
    linkArr.append(linkObject)
#takes the title and author of the first 5 search results and adds it to the linkArr array

print(linkArr)
print(entryLink)

whichLink = int(input("Which book do you want? 1/2/3/4/5  "))

if whichLink == 1:
    THElink = entryLink[0]
    print(THElink)
elif whichLink == 2:
    THElink = entryLink[1]
    print(THElink)
elif whichLink == 3:
    THElink = entryLink[2]
    print(THElink)
elif whichLink == 4:
    THElink = entryLink[3]
    print(THElink)
elif whichLink == 5:
    THElink = entryLink[4]
    print(THElink)
else:
    print("Enter a number between 1 and 5")

