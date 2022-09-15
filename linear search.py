ls=[]
n=int(input('Enter the number of elements: '))
for i in range(n):
    l=int(input('Enter the element: '))
    ls.append(l)
k=int(input('enter the element to be searched: '))
for i in range(n):
    if int(ls[i] == k):
        print('SEARCH SUCESSFULL!')
        print(f'{k} is found at {i+1}th position!')
        exit(0)
print('UNSUCESSFULL SEARCH!')
print('Entered key is not found in your listed elements')