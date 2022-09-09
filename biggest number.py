n=int(input('Enter the number of elements: '))
list=[]
for i in range(n):
    ele=input('Enter the number: ')
    list.append(ele) 
list.sort()
print(f"biggest number is {list[-1]}")