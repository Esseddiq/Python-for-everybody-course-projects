import urllib.parse,urllib.request,json
url_service='https://py4e-data.dr-chuck.net/opengeo?'
addresse=input("enter your addresse?")
parms={}
parms['q']=addresse
url= url_service +urllib.parse.urlencode(parms) 
print("Retrieved url:" ,url)
with urllib.request.urlopen(url) as requested_data:
         data=requested_data.read().decode()
try:
         js=json.loads(data)
except:
         js=None
if not js or 'features' not in js:
     print("Failed to retrieve!!")
     print(data)
     quit()
if len(js['features'])==0:
     print("Elements not found!")
     print(data)
     quit()
plus_code=js["features"][0]["properties"]["plus_code"]
print("plus_code:",plus_code)

    
     


    #here using json.dumps it could take other parameters to control 
    # the son string format is the opposite of json.loads 
raw_location=json.dumps(js['features'][0]['properties']['formatted'],indent=4)
print(raw_location)

    #latt=js['features'][0]['properties']['lat']
    #lon=js['features'][0]['properties']['lon']
    #location=js['features'][0]['properties']['formatted']
    #print("latt=",latt, "lon",lon)
    #print("Location:", raw_location)

