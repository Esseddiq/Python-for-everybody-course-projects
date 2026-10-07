import urllib.request,urllib.parse,urllib.error
import re
url=input("enter the url page?")
response=urllib.request.urlopen(url).read()
links=re.findall(b'href="(http[s]?://.*?)"',response)
for link in links:
    print(link.decode())