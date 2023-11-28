list1=list(eval(input(" Enter the Elements = ")))
max=list1[0]
min=list1[0]
for i in list1:
    if max<i:
        max=i
    if min>i:
        min=i
print(max,min)