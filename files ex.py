# with open('antitode of life.txt','r',encoding="utf-8-sig") as file:
#     lines=file.readlines()
#     counter=sum(1 for line in lines if line.strip().startswith('Rule'))
#     print("there ares",counter,"lines that start with (Rule) in the this file")
#     for line in lines:
#         line = line.rstrip()
#         if line.lstrip().startswith('Rule'):
#             print(line)
# handle=open('antitode of life.txt','r',encoding="utf-8-sig") 
# for line in handle:
#     line=line.rstrip()
#     if 'self' not in line:
#         continue
#     print(line)
fname=input("please enter a file name?")
fopen=open(fname,'r',encoding='utf-8-sig')
#counter=0
# for line in fopen:
#     if "Rule"  in line:
#         print(line,'\n')
#         counter=counter+1
# print('the word rule is repeted',counter,'times in this file')

fopen.seek(15)
print(fopen.read(9))


        
    

    