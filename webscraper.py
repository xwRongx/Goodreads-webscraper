from bs4 import BeautifulSoup
import requests
import json
#imports libraries needed

bookLink = "40545956-where-the-forest-meets-the-stars"
#will have user input link, later on will make search function that automatically gets link 
url = 'https://www.goodreads.com/book/show/' + bookLink
response = requests.get(url, timeout=5)  
content = BeautifulSoup(response.content, "html.parser")
#saves the entire html from the website into content variable

#later on will do multiple books, saved and include input if this book (title, author, stars) is the one.
#if yes then print all 6 categories and maybe "get a copy" link to kindle/amazon/stores

#finds the text for the title, author, stars, etc. from content variable
#saves text from tag as a value in a dictionary
bookObject = {
    "title": content.find("h1", attrs={"id": "bookTitle"}).text,
    "author": content.find("span", attrs={"itemprop":"name"}).text,
    "stars": content.find("span", attrs={"itemprop":"ratingValue"}).text,
    "ratings": content.find("meta", attrs={"itemprop":"ratingCount"}).text,
    "reviews": content.find("meta", attrs={"itemprop":"reviewCount"}).text,
    "summary": content.find("div", attrs={"id":"description"}).text
}
#format- category: scraped information from html but without the tags

for i in bookObject:
     print(i + ":" + bookObject[i])
#prints the category:info

#minor problems: weird spacing from og html, full summary is printed but w/ "...more" from the link

with open('goodreadsInfo.json', 'w') as outfile:
    json.dump(bookObject, outfile)
#saves the dictionary bookObject to json file



