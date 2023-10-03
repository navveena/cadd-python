try:
    a=78
    b=788
    assert a==b

except AssertionError:
    print("assertion exception raised.")
else:
    print("success,no error!")
    