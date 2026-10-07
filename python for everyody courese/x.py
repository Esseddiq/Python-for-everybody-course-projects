#1)creating a dictionnary through lists

names=["Esseddiq","Ismail","Esseddiq","Moad","Esseddiq","Asmaa","Esseddiq","Moad"]
counts={}
for name in names:
   counts[name]=counts.get(name,0)+1
    # if name not in counts:
    #     counts[name]=1
    # else:
    #     counts[name]=counts[name]+1
print(counts)

#2)looping though the dictionnary using tow variables

for a,b in counts.items():
   print(a,b)