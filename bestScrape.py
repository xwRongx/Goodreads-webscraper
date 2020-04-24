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

bestArr = []
bestObject = {}

def bestScrape():
    responsebest = requests.get(url + urlbest + str(urlyear), timeout=5)  
    contentbest = BeautifulSoup(responsebest.content, "html.parser")
    #setup: url is the url searchbar takes you to

    for entry in contentbest.findAll('div', attrs={'class': 'category clearFix'}):
        bestObject = {
            "genre": entry.find('h4', attrs={'class': 'category__copy'}).text,
            "link": entry.find('a', attrs={'href': re.compile('^/choiceawards/best-')}).get('href')

            #to choice book page to get #votes
        }
        bestArr.append(bestObject)
        
    print(bestArr)

'''PROBLEM SOLVED: how to get links. Use regular expression to find links that start with certain thing-will 
take entire a tag. only want link so .get('href') to take ONLY the link'''
bestScrape()

def bestInfo():
    for award in bestArr:
        print(bestArr)
        print(url + bestObject['link'])
        responsebestinfo = requests.get(url + bestObject["link"], timeout=5)  
        contentbestinfo = BeautifulSoup(responsebestinfo.content, "html.parser")
        #goes to link of specific award page

bestInfo()
        


'''
with open('bestScrapedata.json', 'w') as outfile:
    json.dump(bestArr, outfile)'''


