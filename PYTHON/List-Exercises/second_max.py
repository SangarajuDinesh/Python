list1=list(map(int,input().strip().split()))
second_max=list1[0]
max=list1[0]
for i in list1:
    if max<i:
        second_max=max
        max=i
    if second_max<i and max!=i:
        second_max=i
print(second_max)