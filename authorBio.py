from bs4 import BeautifulSoup
import requests
import json
import re
#imports libraries needed

urlauthorpage = '/author/show/'
urlauthor = "2778055"

#will have user input an author's name, their basic information will show up
url = 'https://www.goodreads.com'
responseauthor = requests.get(url + urlauthorpage + urlauthor, timeout=5)  
contentauthor = BeautifulSoup(responseauthor.content, "html.parser")
#saves the entire html from the website into content variable

#later on will find for different authors, saved and include input if this author is the one.
#if yes then print all 6 categories and maybe "get a copy" link to kindle/amazon/stores

#finds the text for the author's name, birth date, etc. from content variable
#saves text from tag as a value in a dictionary
authorObject = {
    "birth name": contentauthor.find("h1", attrs={"class": "authorName"}).text,
    "birth date": contentauthor.find("div", attrs={"itemprop": "birthDate"}).text,
    "death date": contentauthor.find("div", attrs={"itemprop": "deathDate"}).text,
    "genre": contentauthor.find("a", attrs={"href": re.compile('^/genres/')}).text,
    "information": contentauthor.find("div", attrs={"class": "aboutAuthorInfo"}).text,
}
#format- category: scraped information from html but without the tags

for i in authorObject:
     print(i + ":" + authorObject[i])
#prints the category:info

#minor problems: weird spacing from og html, full summary is printed but w/ "...more" from the link

with open('goodreadsInfo.json', 'w') as outfile:
    json.dump(authorObject, outfile)
#saves the dictionary authorObject to json file