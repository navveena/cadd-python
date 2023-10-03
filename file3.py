try:
    f1=open("E:\\exam2.txt",'r')
    str=f1.readline(7)
    print(str)

except IOError:
    print("file not found error")