n=input("Enter the String = ")
m=n.split(' ')
max=m[0]
for i in m:
    if len(max) < len(i):
        max=i
print(max)