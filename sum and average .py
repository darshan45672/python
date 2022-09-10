sum=0.0
count=0
while True:
    number=float(input('enter the number: '))
    sum+=number
    count+=1
    chioce=input('add another number?  ( y/n ) ')
    if chioce.lower()=="n":
        break
    elif chioce.lower()=="y":
        continue
    elif chioce.lower()!="n":
        break
    else:
        break
print('sum '+str(sum))
print('average is '+str(sum/count))
