name=list(eval(input("Enter the words sepersted by comma = ")))
max=name[0]
for i in name:
    if len(max)<len(i):
        max=i
print(max)
