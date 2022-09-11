r=int(input('Enter the number of row: '))
c=int(input('Enter the number of columns: '))
mtrx=[]
for i in range(r):
    a=[]
    for j in range(c):
        k=input('Enter the elements for your matrix: ')
        a.append(k)
    mtrx.append(a)
for i in range(r):
    for j in range(c):
        print(mtrx[i][j], end=" ")
    print()