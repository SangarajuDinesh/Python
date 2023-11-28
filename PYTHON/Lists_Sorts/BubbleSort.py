list1=list(map(int, input().strip().split()))
for i in range(len(list1)-1):
    for j in range(len(list1)-i-1):
        if list1[j]>list1[j+1]:
            num=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=num
print(list1)