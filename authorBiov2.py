from bs4 import BeautifulSoup

import requests

import json

#imports libraries needed



authorLink = "2778055.Kurt_Vonnegut"

#will have user input an author's name, their basic information will show up

url = 'https://www.goodreads.com/author/show/' + authorLink

response = requests.get(url, timeout=5)  

content = BeautifulSoup(response.content, "html.parser")

#saves the entire html from the website into content variable



#later on will find for different authors, saved and include input if this author is the one.

#if yes then print all 6 categories and maybe "get a copy" link to kindle/amazon/stores



#finds the text for the author's name, birth date, etc. from content variable

#saves text from tag as a value in a dictionary

authorObject = {

    "birth name": content.find("h1", attrs={"class": "authorName"}).text,

    "birth date": content.find("div", attrs={"itemprop": "birthDate"}).text,

    "death date": content.find("div", attrs={"itemprop": "deathDate"}).text,

    "genre": contentauthor.find("a", attrs={"href": re.compile('^/genres/')}).text,

    "information": content.find("div", attrs={"class": "aboutAuthorInfo"}).text,

}

#format- category: scraped information from html but without the tags



for i in authorObject:

     print(i + ":" + authorObject[i])

#prints the category:info



#minor problems: weird spacing from og html, full summary is printed but w/ "...more" from the link



with open('goodreadsInfo.json', 'w') as outfile:

    json.dump(authorObject, outfile)

#saves the dictionary authorObject to json file
