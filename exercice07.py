fname=input("please enter the file name?\n")
try:
    fopen=open(fname,'r',encoding='utf-8-sig')
except:
    print('the',fname," file can't be open")
    quit()
size_to_read=input("please enter the amount of characters that you want to read from the file?")
try:
    isize_to_read=int(size_to_read)
except:
    print("please enter an integer!!\n")
    quit()
print("here is the first",isize_to_read,"characters from the",fname,"file:")
print(fopen.read(isize_to_read))