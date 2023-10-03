try:
    a=100/0
    print(a)
except ZeroDivisionError:
    print("zero division exception raised")
else:
    print("success")