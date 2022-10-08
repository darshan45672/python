n=int(input('Enter a number: '))
def fizz_buzz(n):
    if(n%3==0)and(n%5==0):
        return "Fizz_Buzz"
    if n%3==0:
        return "Fizz"
    if n%5==0:
        return "Buzz"
    return n
print(fizz_buzz(n))