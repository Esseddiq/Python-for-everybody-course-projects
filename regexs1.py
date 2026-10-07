import re
# with open('mbox-short.txt','r',encoding='utf-8-sig') as file:
#     numlist=[]
#     emailslist=[]
#     for line in file:
#         line=line.rstrip()
#         emails = re.findall(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
#         staf=re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#         if len(staf) == 1:
#             num=float(staf[0])
#             numlist.append(num)
#         elif len(emails) > 0:
#             emailslist.extend(emails)
#     uniqueemailslist=list(set(emailslist))
#     print("Maximum:",max(numlist),"\n")
#     print(f"we have {len(uniqueemailslist)} unique emails")
#     print("\n")
#     print(uniqueemailslist)
#     print("\n")
# with open('mbox-short.txt','r',encoding='utf-8-sig') as file:
#     for line in file:
#         line=line.rstrip()
#         hour=re.findall(r'From .* ([0-9][0-9]):' , line)
#         if len(hour)==1:
#             print(hour)
# with open('mbox-short.txt','r',encoding='utf-8-sig') as file:
#     numberslist=[]
#     for line in file:
#         line=line.rstrip()
#         search=re.findall(r'^New \S+: ([0-9]+)' , line)
#         if len(search)==1:
#             number=int(search[0])
#             numberslist.append(number)
#     avrg=sum(numberslist)/len(numberslist)
#     print(avrg)
with open('regex project2.txt','r',encoding='utf-8-sig') as file:
    data=file.read()
    prase=re.findall(r'[0-9]+' , data)
    if prase:
        numberslist=([int(number) for number in prase])
    print(f'sum2={sum(numberslist)}')
            

