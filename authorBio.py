from bs4 import BeautifulSoup
import requests
import json
#imports libraries needed

urlpage = '/book/show/'
urlauthor = "2778055"

#will have user input an author's name, their basic information will show up
url = 'https://www.goodreads.com'
response = requests.get(url + urlpage + urlauthor, timeout=5)  
contentauthor = BeautifulSoup(response.content, "html.parser")
#saves the entire html from the website into content variable

#later on will find for different authors, saved and include input if this author is the one.
#if yes then print all 6 categories and maybe "get a copy" link to kindle/amazon/stores

#finds the text for the author's name, birth date, etc. from content variable
#saves text from tag as a value in a dictionary
authorObject = {
    "birth name": content.find("span", attrs={"itemprop": "name"}).text,
    "birth date": content.find("div", attrs={"class": "birthDate"}).text,
    "birth place": content.find("div", attrs={"class": "dataTitle"}).text,
    "death date": content.find("div", attrs={"class": "deathDate"}).text,
    "genre": content.find("div", attrs={"class": "dataItem"}).text,
    "information": content.find("div", attrs={"class": "aboutAuthorItem"}).text,
}
#format- category: scraped information from html but without the tags

for i in authorObject:
     print(i + ":" + authorObject[i])
#prints the category:info

#minor problems: weird spacing from og html, full summary is printed but w/ "...more" from the link

with open('goodreadsInfo.json', 'w') as outfile:
    json.dump(authorObject, outfile)
#saves the dictionary authorObject to json file