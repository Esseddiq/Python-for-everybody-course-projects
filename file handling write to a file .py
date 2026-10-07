lines=["RULE1: lif is to take responsibility","RULE2: make big sacrifeces and never count if your reasons are right","RULE3: don't chase your impulses build for your long term vision","RULE4: stay focused"]
with open('newwritefile.txt','w',encoding='utf-8-sig') as file1:
    for line in lines:
        file1.write(line+'\n')
with open('newwritefile.txt','r',encoding='utf-8-sig') as readfile1:
    print(readfile1.read())
