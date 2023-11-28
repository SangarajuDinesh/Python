n=input("Enter the string = ")
for i in n:
    if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
        n=n.replace(i,'*')
print(n)