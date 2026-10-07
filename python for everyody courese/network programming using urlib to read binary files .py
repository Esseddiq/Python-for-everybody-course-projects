import urllib.request,urllib.parse,urllib.error

#1)in this program we will read all the data at once
# and rewrite into anther img file 

img=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
imgfile=open('p4e main page image.png','wb')
imgfile.write(img)
imgfile.close()

#2)here we will read the data partiely and rewrite it with the same %
#in this program we simply buffer to avoid memory problems if we 
#are handling a data > to our computer storage 

data=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
handle=open('p4e image.jpg','wb')
size=0
while True:
    recv=data.read(100000)
    size=size+len(recv)
    if len(recv)<1:
        break
    handle.write(recv)
print(f"the size of the data is {size}")
    

        