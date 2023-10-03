try:
    import math
    print(math.exp(1000))
except OverflowError:
    print("overflow exception raised")
else:
    print("success,no eror!")

    