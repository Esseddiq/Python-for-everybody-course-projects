import urllib.request , urllib.parse , urllib.error
phand=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts={}
for line in phand:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
import bs4 


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
