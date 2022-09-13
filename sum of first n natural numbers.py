from re import I


n=int(input('Enter the number upto which you want to determine the sum: '))
i=1
sum=0.0
for i in range(0,n+1):
    sum += i
print(f'The sum of first {n} natural numbers is {sum}')