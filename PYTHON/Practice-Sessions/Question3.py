inp1=input("Enter the String containing some digits = ")
sum=0
for i in inp1:
    if i.isdigit():
        sum+=int(i)
print(sum)

