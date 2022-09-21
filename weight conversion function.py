def weightk():
    converted = wght/0.45
    print("your weight in lbs is "+str(converted))
def weightlbs():
    cnvrt=wght*0.45
    print("your weight in kilograms is "+str(cnvrt))
wght =int(input('Enter your weight: '))
unit=input('wether is in kilogram (k) or lbs (l)?')
if unit.upper()=="K":
    weightk()
else:
    weightlbs()