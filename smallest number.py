n=int(input('Enter the number of elements: '))
list=[]
for i in range(n):
    ele=float(input('Enter a number: '))
    list.append(ele)
list.sort()
print(f'Smallest number is {list[0]}')