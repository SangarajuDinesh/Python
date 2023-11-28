l=list(eval(input("Enter the elements seperated by comma ")))
last=l[-1]
for i in range(len(l)-1,0,-1):
    l[i]=l[i-1]
l[0]=last
print(l)