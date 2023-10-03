try:
    a=['a','b','c']

    print(a[4])
except LookupError:
    print("index error exception raised,list index out of range")
else:
    print("success,no error!")
