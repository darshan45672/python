mylist=[]
n=int(input('Enter the number of elements: '))
for i in range(n):
    ele=float(input('Enter the number: '))
    mylist.append(ele)
mylist.sort()
print(f'Smallest number is {mylist[0]}')
print(f'Largest number is {mylist[-1]}')