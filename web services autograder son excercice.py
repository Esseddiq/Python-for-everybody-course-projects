import urllib.request,urllib.parse
import json
url=input("enter json data url?")
requesteddata=urllib.request.urlopen(url)
data=requesteddata.read().decode()
print(f"Retrieved {len(data)} characters")
numberslist=[]
js=json.loads(data)
for comment in js["comments"]:
   numberslist.append(comment["count"])
print("sum:",sum(numberslist))