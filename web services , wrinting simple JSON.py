import json

#1)simple hand wirted JSON code

data='''
{
 "name":"Esseddiq",
 "phone":{
          "type":"intl",
          "number":"+212 627012836"
          },
 "email":{
          "hide":"yes"
         } 
}
'''
infos=json.loads(data)
print("Name:" ,infos["name"])
print("Phone_nmber:" ,infos["phone"]["number"])
print("\n\n")
#2)a little advanced one

inputed='''
[
  {
    "id":"001R",
    "age":23,
    "name":"Esseddiq"
  },
  {
    "id":"005W",
    "age":28,
    "name":"Moad"
  }
]
'''
users=json.loads(inputed)
print("Users number:" ,len(users),"\n")
counter=0
for user in users:
    counter+=1
    print(f"user{counter} infos...")
    print("Name:" ,user["name"])
    print("ID:" ,user["id"])
    print("Age:" ,user["age"])
    print("\n")
