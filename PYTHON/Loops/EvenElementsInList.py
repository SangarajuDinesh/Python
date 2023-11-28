count=int(input("Enter the No.of Elements = "))
list1=[]
for i in range(count):
    ele=int(input("Enter the Element data = "))
    list1.append(ele)
list2=[]
for i in list1:
    if i%2==0:
        list2.append(i)
print(list2)