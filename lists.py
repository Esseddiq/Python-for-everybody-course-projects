# numbers=list()
# counter=0
# while True:
#     strvalue=input("please enter a number ")
#     if strvalue=="done".lower():
#         print("done")
#         break
#     try:
#         value=float(strvalue)
#     except:
#         print("please enter a real number!!")
#         counter=counter+1
#         continue
#     numbers.append(value)
# print(f"you've entered {len(numbers)} numbers")
# print(f"the sum of the numbers you've entered is: {sum(numbers)}")
# print(f"and thier average is: {sum(numbers)/len(numbers)}")
# print(f"the smalest number you've entered is: {min(numbers)}")
# print(f"the bigest number you've entered is: {max(numbers)}")
# print(f"you've entered wrong values {counter}times")


# fopen=open('mbox-short.txt')
# for line in fopen:
#     words=line.split()
#     if len(words)<5:
#         continue
#     if  line.startswith('From'):
#         #print(line)
#         print(words[2])

# sentence="please love others but don't expect them to give it back to you?"
# # listed=list(sentence)
# # print (listed)
# #if we want to turn strings into list we can use the .split(delimeter) function
# #if we want to turn list to normal strings we can use .join(delimeter) function
# splited= sentence.split()
# print(splited)
# desplited=splited.join("")
# print(desplited)

# g=['dont','love','to','too','much']
# normal=' '.join(g)
# print(normal)


# def delete_head(t):
#     del t[0]

# letters = ['a', 'b', 'c']
# delete_head(letters)
# print(letters)

# def tail(x):
#     return x[1:]
# letter =['k','r','w','y']
# rmv=tail(letter)
# print(rmv)

# def chop(lst):
#     if len(lst)>1:
#         del lst[0]
#         del lst[-1]
#     elif len(lst)==1:
#         del lst[0]
#     return None
# def midle(st):
#     return st[1:-1]
# st=[45,98,24,94,12]
# print(midle(st))

fhand = open('mbox-short.txt','r',encoding='utf-8-sig')
for line in fhand:
    words = line.split()
    if len(words)==0:continue
    if words[0] != 'From': continue
    print(words[2])