try:
    f1=open("d:\\ss1222.txt","w")
    f1.write("hai i am sundar")
    print("file created and written successfully")
except IOError:
    print("file exception occured")
finally:
    print("memory is cleaned perfectly")

    