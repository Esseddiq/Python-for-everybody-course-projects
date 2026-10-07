import urllib.request,urllib.parse,urllib.error

#like socket urllib when we get the response forn the server we get the headers
#but the .urlopen is going to eat then they won't show up in the response

filerequest=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
dic={}
for line in filerequest:
    words=line.decode().rstrip().split()
    for word in words:
        dic[word]=dic.get(word,0)+1
print(dic)

htmlrequest=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read()
print(htmlrequest.decode())