import requests
from bs4 import BeautifulSoup
import json
import re
#imports libraries

url = 'https://www.goodreads.com' 
urlbest = '/choiceawards/best-books-'
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

<<<<<<< Updated upstream
response = requests.get(url + urlbest + str(urlyear), timeout=5)  
contentbest = BeautifulSoup(response.content, "html.parser")
#setup: url is the url searchbar takes you to

bestArr = []
=======
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
>>>>>>> Stashed changes

for entry in contentbest.findAll('div', attrs={'class': 'category clearFix'}):
    bestObject = {
        "genre": entry.find('h4', attrs={'class': 'category__copy'}).text,
        "link": entry.find('a', attrs={'href': re.compile("^/choiceawards/best-")}).get('href')
        #to choice book page to get #votes
    }
    bestArr.append(bestObject)

<<<<<<< Updated upstream
for entrygenre in bestArr
'''
with open('bestScrapedata.json', 'w') as outfile:
=======
'''with open('bestScrapedata.json', 'w') as outfile:
>>>>>>> Stashed changes
    json.dump(bestArr, outfile)'''


