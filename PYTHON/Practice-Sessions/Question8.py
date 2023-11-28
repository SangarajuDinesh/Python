n=input("Enter the String = ")
m=""
for i in range(len(n)-1,-1,-1):
    m+=n[i]
print(m)