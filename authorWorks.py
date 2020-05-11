from bs4 import BeautifulSoup
import requests
#for storing data as json:
import json
import re

url ='https://www.goodreads.com/author/show/4919495.Chris_Colfer?from_search=true&from_srp=true'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

dateArr = []
#makes an array

#for date in content.findAll('p', attrs={"class": "content"}):
    #print(date.text.encode('utf-8'))
#prints all dates and titles of books

for date in content.findAll('tr', attrs={"itemtype": "http://schema.org/Book"}):
    dateObject = { 
    'rating':date.find("span", attrs={"class":"minirating"}).text,
    'title': date.find('span', attrs={'itemprop': 'name'}).text
    }
    #make a dictionary with all the info you want
    #print(dateObject)
    dateArr.append(dateObject)
    #adds dateObject to dateArr array


for work in dateArr:
     print('Title: ' + work['title'])
     print('Rating: ' + work['rating'] + '\n')

with open('dateData.json', 'w') as outfile:
    json.dump(dateArr, outfile)
    #makes json file "dateData" and puts dateArr into it