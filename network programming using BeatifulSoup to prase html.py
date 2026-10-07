import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import requests 

#1)html parsing project using BeatifulSoup only

# url=input("enter th url of the eb page?")
# response=requests.get(url)
# Soup=BeautifulSoup(response.text,'html.parser')
# for tag in Soup.find_all('a'):
#     print(tag.get('href'))

#2)html parsing project using BeatifulSoup with urllib

iurl=input("enter the web page url?")
binary_content=urllib.request.urlopen(iurl).read()
soup=BeautifulSoup(binary_content,'html.parser')
spans = soup.find_all("span", class_="comments")
numbers = []
for span in spans:
    value = int(span.text)
    numbers.append(value)
print(sum(numbers))
