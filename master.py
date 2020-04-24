'''
Title: Goodreads Webscraper
Authors: Rose Wong and Pauline Wang
AP CSP 2019-2020 CREATE Task
'''

from bs4 import BeautifulSoup
import requests
import json
import re
#imports libraries

intro = int(input('''Hello! What do you want the goodreads webscraper to do?
1. search for a book
2. author bio
3. author's works
4. best book of the year nominees
5. best book of the year winners
6. quote generator
:      '''))

url = 'https://www.goodreads.com'
urlpage = '/book/show/'
urlsearch = '/search?q='
#common url headings of goodreads pages; concatenated with page specific urls in function

def searchScrape(): 
    urlsearchTerm = input("What book do you want to search for?")
    #asks user to enter a book name

    response = requests.get(url + urlsearch + urlsearchTerm, timeout=5)  
    contentsearch = BeautifulSoup(response.content, "html.parser")
    #setup: url is the url searchbar takes you to
    #concatenates goodreads url, search url, and specific book name url 
    # can directly add book name to search term because search url contains it
    #for book and author pages, specific url is a series of numbers

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



if intro == 1:
    searchScrape()
elif intro == 2:
    authorbio()
elif intro == 3:
    asd
elif intro == 4:
    sfs
elif intro == 5:
    sfs
elif intro == 6:
    sfs
#decides which function to call according to what the user replied in intro; must be at the end because function must be defined before calling