try:
    number=float(input("enter any float value"))
except ValueError:
    print('invalid input')
else:
    print('success')



try:
    a=100/100
    print(a)
except ZeroDivisionError:
    print('divide by zero')
else:
    print('success')