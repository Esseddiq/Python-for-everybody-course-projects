import socket
try:
   url=input("enter url page?")
except OSError:
    print("The requested address is not valid in its context")
    quit()
hostlst=url.split('/')
#create a socket object
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#conect the object to the server endpoint
mysocket.connect((hostlst[2],80))
#create an HTTP GETrequest and send it to the server
therequest=f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysocket.send(therequest)


#the server is going to prosseces the the request and send us the data back 

while True :
    data=mysocket.recv(521)
    if (len(data))<1:
        break
    print(data.decode())

