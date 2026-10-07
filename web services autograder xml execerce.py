import urllib.request
import xml.etree.ElementTree as ET
url=input("enter the xml url?")
raw=urllib.request.urlopen(url)
xmldata=raw.read().decode()
print(f"Retrieved {len(xmldata)} characters")
data=ET.fromstring(xmldata)
counts_lists=data.findall('comments/comment/count')
numbers_list=[]
for number in counts_lists:
    integer=int(number.text)
    numbers_list.append(integer)
print("sum=",sum(numbers_list))


