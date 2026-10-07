fname=input("please enter the file name?")
try:
    fopen=open(fname,'r',encoding='utf-8-sig')
except:
    print(f"{fname} doesn't exist!!")
    quit()
counter=0
total_points=0
for line in fopen:
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        try:
             slicing=line[18+2:]
             floating=float(slicing)
             counter+=1
             total_points=total_points+floating
        except ValueError:
                continue
fopen.close()
if counter>0:
    print(f"there is{counter}lines like this (X-DSPAM-Confidence: 0.8475) in this file")
    print(f"the average of the floating points in these lines is:{total_points/counter}")
else:
     print("there is no such lines in this files!!")

