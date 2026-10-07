import xml.etree.ElementTree as ET

#1)simple write hand code xml

# data='''
# <person> 
#    <name> Esseddiq </name>
#    <phone type="intl"> 
#       +212 627012836
#    </phone>
#    <email hide="yes"/>
# </person>
# '''
# tree=ET.fromstring(data)
# print("Name:" ,tree.find("name").text)
# print("attribute:" ,tree.find("email").get("hide"))

#2)a little advanced write handed xml code

inputed='''
<sttaf>
    <users>
       <user x='2'>
           <name> Esseddiq </name>
           <id> 001 </id>
        </user>
        <user x='7'>
           <name> Moad </name>
           <id> 005 </id>
        </user>
    </users>
</sttaf>
'''
formated_xml=ET.fromstring(inputed)
users_list=formated_xml.findall('users/user')
print("Users number:", len(users_list),"\n")
counter=0
for user in users_list:
    counter+=1
    print(f"User{counter} infos:")
    print("Name:" ,user.find("name").text)
    print("ID:" ,user.find('id').text)
    print("X_Attribute:" ,user.get('x'))
    print("\n")