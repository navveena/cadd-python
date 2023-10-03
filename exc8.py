try:
    f1=open("d:\\exgggxxxx.txt","rt")
    print("successfully read")
except IOError:
    print("file not found exception")
else:
    print("file successfully read")

    