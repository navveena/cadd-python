l=[9,8,5,2]
n=len(l)-1
while (n>0):
    
    for i in range(n):
     if (l[i]>l[i+1]):
          l[i],l[i+1]=l[i+1],l[i]
    n=n-1
print(l)
       
       
    

\



