list1=list(map(int,input().strip().split()))
for i in range(len(list1)):
    num=list1[i]
    index=i
    for j in range(i+1,len(list1)):
        if num>list1[j]:
            num=list1[j]
            index=j
    temp=list1[i]
    list1[i]=list1[index]
    list1[index]=temp
print(list1)
