r1=int(input('Enter the number of rows for Matrix 1: '))
c1=int(input('Enter the number of columns for MAtrix 1: '))
mtrx1=[]
print('Matrix 1')
for i in range(r1):
    a=[]
    for j in range(c1):
        k=input('Enter the elements for your matrix: ')
        a.append(k)
    mtrx1.append(a)
for i in range(r1):
    for j in range(c1):
        print(mtrx1[i][j], end=" ")
    print()
r2=int(input('Enter the number of rows for Matrix 2: '))
c2=int(input('Enter the number of columns for MAtrix 2: '))
if (r1!=r2 or c1!=c2):
    print('MATRIX SUBRACTION CANNOT BE PERFORMED!')
    exit(0)
else:
    mtrx2=[]
for i in range(r2):
    a=[]
    for j in range(c2):
        k=input('Enter the elements for your matrix: ')
        a.append(k)
    mtrx2.append(a)
print('Matrix 2')
for i in range(r2):
    for j in range(c2):
        print(mtrx2[i][j], end=" ")
    print()
    result=[]
for i  in range(r1):
    Rs=[]
    for j  in range(c1):
        k= int(mtrx1[i][j])+ int(mtrx2[i][j])
        Rs.append(k)
    result.append(Rs)
print("MATRIX ADDITION")
for i in range(r1):
    for j in range(c1):
        print(result[i][j],end= " ")
    print()
print('THANK YOU!')