list1=list(map(int,input().strip().split()))
for i in range(1,len(list1)):
    num=list1[i]
    j=i-1
    while(j>=0 and list1[j]>num):
        list1[j+1]=list1[j]
        j+=-1
    list1[j+1]=num
print(list1)
