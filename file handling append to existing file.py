with open('newwritefile.txt','a',encoding='utf-8-sig') as to_append:
    to_append.write("RULE5: never try to please others cuase it's going to finish you with losing your self\n")
with open('newwritefile.txt','r',encoding='utf-8-sig') as to_read:
    print(to_read.read())