import string

#1)sorting by keys

d={"a":10,"c":22,"b":1}
print(d.items())
sort=sorted(d.items())
print(sort)
for k,v in sorted(d.items()):
    print(k,v)

#2)sorting by vakues

diction={"Esseddiq":23,"Moad":28,"Ahmed":21,"Rachida":45}
template=[]
for k,v in diction.items():
    template.append((v,k))
sorting=sorted(template , reverse=True)
print(sorting)

#3)applying it to a file

finput=input("enter the file?\n")
fopen=open(finput,'r',encoding='utf-8-sig')
counts={}
for line in fopen:
    line=line.rstrip()
    line=line.translate(line.maketrans("","",string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

#3.1)sorting the list of tupeles using the traditionel way

# empthy=[]
# for k,v in counts.items():
#     empthy.append((v,k))
# sortedlist=sorted(empthy,reverse=True)
# for v,k in sortedlist[:10]:
#     print(v,k)

#3.2)sorting the list of tupeles using list comprehension way

sortedlist=sorted([(v,k) for k,v in counts.items()],reverse=True)
for v,k in sortedlist[:10]:
    print(k,v)


