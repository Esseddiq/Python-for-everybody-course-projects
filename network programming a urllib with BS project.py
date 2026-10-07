import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl 

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input("entr count?"))
position=int(input("enter position?"))
for repeat in range(count):
      html = urllib.request.urlopen(url, context=ctx).read()
      soup = BeautifulSoup(html, 'html.parser')
      tags = soup('a')
      final_tag=tags[position-1].get('href')
      print(f"Retrieving: {final_tag}")
      url=final_tag
print(tags[position-1].contents[0])

