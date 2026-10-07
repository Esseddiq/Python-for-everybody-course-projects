import urllib.request,urllib.parse,urllib.error,json
service_url="http://py4e-data.dr-chuck.net/json?"
while True:
    addresse=input("enter your addresse?")
    if len(addresse)<1:break
    url=service_url+urllib.parse.urlencode({'addresse':addresse})
    print("Retrieving url:" ,url)
    requested_data=urllib.request.urlopen(url)
    data=requested_data.read().decode()
    try:
        js=json.loads(data)
    except:
        js=None
    if not js or 'status' not in js or js['status']!='ok':
        print("failure to retrieve")
        print(data)
        continue
    lat=js['results'][0]['geometry']['location']['lat']
    print(lat)
    
    