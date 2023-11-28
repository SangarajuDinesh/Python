l=list(eval(input("Enter the elements seperated by comma = ")))
m=list(eval(input("Enter the elements seperated by comma = ")))
N=[]
for i in range(len(l)):
    N.append(l[i]+m[i])
print(N)