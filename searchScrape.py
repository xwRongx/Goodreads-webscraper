import requests
from bs4 import BeautifulSoup
import json
import re
#imports libraries


searchTerm = input("What book do you want to search for?")
#asks user to enter a book name

url = 'https://www.goodreads.com' + '/search?q=' + searchTerm
response = requests.get(url, timeout=5)  
contentsearch = BeautifulSoup(response.content, "html.parser")
#setup: url is the url searchbar takes you to

entryLink = []

for link in content.findAll('a', attrs={"class": "bookTitle"}, limit=5):
    entryLink.append('www.goodreads.com' + link.get('href'))
#takes the first 5 links on the page with the class bookTitle
#adds the goodreads url to the link path and appends it to the entryLink list 

linkArr = []

for tr in content.findall('li', attrs={"class": "book"}, limit=5):
    linkObject = {
        "title": content.find("span", attrs={"role": "heading"}).text,
        "author": content.find("span", attrs={"itemprop":"author"}).text,
    }
    linkArr.append(linkObject)
#takes the title and author of the first 5 search results and adds it to the linkArr array

print(linkArr)

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
#asks user which result is the one they are looking for then prints it
