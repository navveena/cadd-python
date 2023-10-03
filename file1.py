try:
    f1=open("E:\\exam2.txt",'w')
    f1.write("welcome to caddcae")

except IOError:
    print("file not found error")
    