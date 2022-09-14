def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input('Enter a INTEGER: '))
if n>0:
    print(fact(n))
else:
    print('FACTORIAL FUNCTION IS NOT VALID FOR NEGEATIVE INTEGERS!')
print('THANK YOU!')