'''
Title: Goodreads Webscraper
Authors: Rose Wong and Pauline Wang
AP CSP 2019-2020 CREATE Task
Due Date: May 26, 2020
'''

from bs4 import BeautifulSoup
import requests
import json
import re
#imports libraries

intro = input('''Hello! What do you want the goodreads webscraper to do?
1. search for a book
2. author biography and works
3. best book of the year winners
:      ''')

url = 'https://www.goodreads.com'
urlpage = '/book/show/'
urlauthorpage = '/author/show/'
urlsearch = '/search?q='
urlbest = '/choiceawards/best-books-'
#common url headings of goodreads pages; concatenated with page specific urls in function

def searchScrape(): 
    urlsearchTerm = input("What book do you want to search for?")
    #asks user to enter a book name

    responsesearch = requests.get(url + urlsearch + urlsearchTerm, timeout=5)  
    contentsearch = BeautifulSoup(responsesearch.content, "html.parser")
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

def authorBio():
    urlauthor = input("What author do you want to search for?")
    urlauthor = "2778055"

    responseauthor = requests.get(url + urlauthorpage + urlauthor, timeout=5)  
    contentauthor = BeautifulSoup(responseauthor.content, "html.parser")

    #finds the text for the author's name, birth date, etc. from contentauthor variable
    #saves text from tag as a value in a dictionary
    authorObject = {
        "birth name": contentauthor.find("h1", attrs={"class": "authorName"}).text,
        "birth date": contentauthor.find("div", attrs={"itemprop": "birthDate"}).text,
        "death date": contentauthor.find("div", attrs={"itemprop": "deathDate"}).text,
        "genre": contentauthor.find("a", attrs={"href": re.compile('^/genres/')}).text,
        "information": contentauthor.find("div", attrs={"class": "aboutAuthorInfo"}).text,
    }
    #format- category: text from scraped html

    for i in authorObject:
        print(i + ": " + authorObject[i])
    #prints the category:info
    

    dateArr = []

    for date in contentauthor.findAll('tr', attrs={"itemtype": "http://schema.org/Book"}):
        dateObject = { 
        'rating':date.find("span", attrs={"class":"minirating"}).text,
        'title': date.find('span', attrs={'itemprop': 'name'}).text
        }
        dateArr.append(dateObject)
        #in each part of the table, it takes the rating and title information

    print('Works:')
    workNumber = 0
    for work in dateArr:
        workNumber += 1
        print(str(workNumber) + '.')
        print('Title: ' + work['title'])
        print('Rating: ' + work['rating'] + '\n')
    #prints titles and ratings of 10 of the author's works in a neat format

def bestScrape():
    urlyear = int(input("Which year do you want to see the best books of?"))
    #url parts that will be used in this function

    if urlyear < 2011:
        print("The goodreads awards did not exist yet at this year!")
        urlyear = int(input("Which year do you want to see the best books of?"))
    elif urlyear > 2019:
        print("The goodreads choice awards for this year does not yet exist!")
        urlyear = int(input("Which year do you want to see the best books of?"))
    else: 
        print("You have chosen the year " + str(urlyear) + ".")
    #asks user to enter a book name

    bestArr = []
    bestObject = {}

    def bestScrape():
        responsebest = requests.get(url + urlbest + str(urlyear))  
        contentbest = BeautifulSoup(responsebest.content, "html.parser")
        #setup: url is the url searchbar takes you to

        for entry in contentbest.findAll('div', attrs={'class': 'category clearFix'}):
            bestObject = {
                "genre": entry.find('h4', attrs={'class': 'category__copy'}).text,
                "link": entry.find('a', attrs={'href': re.compile('^/choiceawards/best-')}).get('href')

                #to choice book page to get #votes
            }
            bestArr.append(bestObject)
            

    '''PROBLEM SOLVED: how to get links. Use regular expression to find links that start with certain thing-will 
    take entire a tag. only want link so .get('href') to take ONLY the link'''
    bestScrape()

        
    #goes to link of specific award page

    whichGenre = int(input("Do you want to see the winners of all genres or a specific genre? 1. all 2. specific genre :  "))

    specificTitle = ''
    specificAuthor = ''
    specificVote = ''

    if whichGenre == 1:
        for award in bestArr:
            responsebestinfo = requests.get(url + award["link"])  
            contentbestinfo = BeautifulSoup(responsebestinfo.content, "html.parser")

            specificTitle = contentbestinfo.find('a', attrs={'class': 'winningTitle'}).text
            specificAuthor = contentbestinfo.find('span', attrs={'itemprop': 'name'}).text
            specificVote = contentbestinfo.find('span', attrs={'class': 'greyText gcaNumVotes'}).text

            print(award['genre'] + ' : ' + specificTitle + ' by ' + specificAuthor + ', ' + specificVote)

    elif whichGenre == 2:
        specificGenre = input("What genre?")

        for f in bestArr:
            if f['genre'] == specificGenre:
                print(f['genre'])
                responsebestinfo = requests.get(url + genre["link"])  
                contentbestinfo = BeautifulSoup(responsebestinfo.content, "html.parser")

                specificTitle = contentbestinfo.find('a', attrs={'class': 'winningTitle'}).text
                specificAuthor = contentbestinfo.find('span', attrs={'itemprop': 'name'}).text
                specificVote = contentbestinfo.find('span', attrs={'class': 'greyText gcaNumVotes'}).text

                print(genre['genre'] + ' : ' + specificTitle + ' by ' + specificAuthor + ', ' + specificVote)


if intro == '1':
    searchScrape()
elif intro == '2':
    authorBio()
elif intro =='3':
    bestScrape()
else:
    print('That\'s not a valid option!')
    exit()
#decides which function to call according to what the user replied in intro; must be at the end because function must be defined before calling