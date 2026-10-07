# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))

# t.sort(reverse=True)
# print(t)
# res = list()
# for length, word in t:
#     res.append(word)

# print(res)

# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = []
# for x in list_of_ints_in_strings:
#     list_of_ints.append(int(x))

# print(sum(list_of_ints))

# int_list=[int(y) for y in list_of_ints_in_strings]
# print(sum(int_list))
# total=None
# def paycount(hours,rate):
#     total = hours*rate
#     return total
# hour=float(input("enter the hours you've worked?"))
# rata=float(input("enter the rate per hour?"))
# print(f"you earn {paycount(hour,rata)}$")



# s = 'pining for the fjords'
# t = s.split()
# print(t)
# ['pining', 'for', 'the', 'fjords']
# print(t[2])


# unique_worsd=[]
# with open("romeo.txt",'r',encoding='utf-8-sig')as fopen:
#     for line in fopen:
#         line=line.rstrip()
#         words=line.split()
#         for word in words:
#             if word in unique_worsd:
#                 continue
#             else:
#                 unique_worsd.append(word)
# unique_worsd.sort()
# print(unique_worsd)


# with open('mbox-short.txt','r',encoding='utf-8-sig') as fhandle:
#     counter=0
#     for line in fhandle:
#         line=line.rstrip()
#         if line.startswith('From '):
#             words=line.split()
#             email=words[1]
#             print(email)
#             counter=counter+1
#         else:
#             continue
# print(f"there are {counter} lines that start with ('From ')")



# with open('mbox-short.txt','r',encoding='utf-8-sig') as fhandle:
#     counter=0
#     for line in fhandle:
#         line=line.rstrip()
#         words=line.split()
#         if len(words)==0 or words[0]!='From':
#             continue
#         elif words[0]=='From':
#             email=words[1]
#             print(email)
#             counter=counter+1
# print(f"there are {counter} lines that start with ('From')")


# nbrs_lst=[]
# while True:
#     strnum=input("enter a number?").lower()
#     if strnum=='done':
#         break
#     try:
#         num=int(strnum)
#     except ValueError:
#         print("Invlid input!!")
#         continue
#     nbrs_lst.append(num)
# if len(nbrs_lst)>0:
#     print(f"Maximum:{max(nbrs_lst)}")
#     print(f"Minimum:{min(nbrs_lst)}")
# else:
#     print("No content to dispplay!!")


# fname = input("Enter file name: ")
# fh=open(fname,'r',encoding='utf-8-sig')
# counter=0
# for line in fh :
#     line=line.rstrip()
#     words=line.split()
#     if len(words)==0 or words[0]!='From':
#         continue
#     elif words[0]=='From':
#         email=words[1]
#         print(email)
#         counter=counter+1
# print(f"there are {counter} lines that start with ('From')")

url="http://data.pr4e.org/romeo.txt"
url_list=url.split('/')
print(url_list)




