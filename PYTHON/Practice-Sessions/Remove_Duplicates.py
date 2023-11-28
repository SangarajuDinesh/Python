lst=list(eval(input("Enter the Elements = ")))
for i in range(len(lst)):
    count=1
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j]:
            count+=1
    if count>=2:
        lst.remove(lst[i])
print(lst)

