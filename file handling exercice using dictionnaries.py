fopen=open('mbox-short.txt','r',encoding='utf-8-sig')
# x="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# words=x.split()
# print(words)
# print(words[2])
emails_count={}
for line in fopen:
    line=line.rstrip()
    if line.startswith("From "):
        words=line.split()
        email=words[1]
        emails_count[email]=emails_count.get(email,0)+1
#print(emails_count)
emailslist=[]
newlist=[]
for k,v in emails_count.items():
    emailslist.append((v,k))
    sorting=sorted(emailslist,reverse=True )
for v,k in sorting:
    newlist.append((k,v))
email,number=newlist[0]
print(email,number)
# mostsender=None
# sendsfreq=None
# for email,count in emails_count.items():
#     if sendsfreq is None or count>sendsfreq:
#         mostsender=email
#         sendsfreq=count
# #print(mostsender,sendsfreq)



