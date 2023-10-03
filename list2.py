l=[5,2,9,8]
n=len(l)
while(n>0):
    i=0
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
        n=n-1
        i=i+1
        print(l)