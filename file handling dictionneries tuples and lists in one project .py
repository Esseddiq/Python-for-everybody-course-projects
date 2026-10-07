fopen=open('mbox-short.txt','r',encoding='utf-8-sig')
# x="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# words=x.split()
# print(words)
# print(words[5][:2])
hours_count={}
for line in fopen:
    line=line.rstrip()
    if line.startswith("From "):
        words=line.split()
        hour=words[5][:2]
        hours_count[hour]=hours_count.get(hour,0)+1
#print(hours_count)
hourslist=sorted([(k,v) for k,v in hours_count.items()])
for k,v in hourslist:
    print(k,v)