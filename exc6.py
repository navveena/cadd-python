try:
    a=int(input("enter any number \n"))
    b=int(input("enter any number \n"))
    c=a/b
    print("the value of a/b is %d " %c)

except ZeroDivisionError:
    print("divide by zero occured")
except ValueError:
    print("u gave a wrong input")
else:
    print("te progress was successfully executed")
