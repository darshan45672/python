n=float(input('Enter your marks: '))
if n>=75:
    print('DISTINCTION!')
elif n>=60 and n<75:
    print('FIRST CLASS!')
elif n>=50 and n<60:
    print('SECOND CLASS!')
elif n>=40 and n<50:
    print('CONGRATULATIONS YOU HAVE PASSED!')
else:
    print('FAIL!')
print('Thank you!')
