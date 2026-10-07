
import string
file_input=input("enter your file?\n")
try:
   fhand=open(file_input,'r',encoding='utf-8-sig')
except FileNotFoundError:
    print("Opps file not found!!")
    exit()
counts={}
for line in fhand:
    line=line.rstrip()
    line=line.translate(line.maketrans("","",string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
print(len(counts))
bigcount=None
bigword=None
for word in counts:
    if counts[word]>100:
        print(word,counts[word])
for word,count in counts.items():
    if bigcount is None or bigcount<count:
        bigword=word
        bigcount=count
print(bigword,bigcount)