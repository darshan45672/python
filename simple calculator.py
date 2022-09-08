num1=float(input('enter first number: '))
num2=float(input('enter second number: '))
print('choose the type of arthematic operations u want to perfoem!')
chioce=input('1. ADDITION(+)   2.SUBRACTION(-)    3.MULTIPLICATION(*)    4.DIVISION(/)     5.MODULO(%) ')
if chioce=="1":
    print('sum '+ str(num1+num2))
elif chioce=="2":
    print('difference '+ str(num1-num2))
elif chioce=="3":
    print('product '+ str(num1*num2))
elif chioce=="4":
        print('quotient '+ str(num1/num2))
else:
    print('remainder '+ str(num1%num2))
print('thank you!')
