import re
#import string
fname=input("enter the file name?\n")
try:
    fread=open(fname,'r',encoding='utf-8-sig')
except FileNotFoundError:
    print(f"the file {fname} you've entered does not exixt\n")
    quit()
#counter1=0
#counter2=0
found=False
wordsdic={}
for line in fread:
    #line = line.translate(str.maketrans('', '', string.punctuation))
    #line=line.rstrip().lower().translate(str.maketrans('','',string.punctuation))
    words = re.findall(r"\b\w+\b", line.lower())
    #words=line.split()
    for word in words:
        if word in wordsdic:
            wordsdic[word]+=1
        else:
             wordsdic[word]=1 
search_word=input("enter the word the you want to count how many times repeated in the file?").lower()
if search_word in wordsdic:
    print(f"the word repeated {wordsdic[search_word]} times in the file named {fname}\n")
    found=True
elif not found:
    print(f"the word {search_word} does not exist in this file!!\n")
print(f"the frequancy of all the words :\n{wordsdic}")
    #count_word=words.count(word)
#if not found:
    #print("the word {word} does not exist in this file!!")
    #quit()
#print(f"the word {word} is repeated {counter2} times in {counter1} lines in the file named {fname}")
      
