list1=list(map(int,input().strip().split()))
max=list1[0]
second_max=list1[0]
for i in range(len(list1)):
    if list1[i]>max:
        second_max=max
        max=list1[i]
    elif(list1[i]>second_max and list1[i]!=max):
        second_max=list1[i]
print(max,second_max)