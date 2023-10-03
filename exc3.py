try:
    a={1:'a',2:'b',3:'c'}
    print(a[4])
except LookupError:
    print("key error exception raised")
else:
    print("success,no error")
    