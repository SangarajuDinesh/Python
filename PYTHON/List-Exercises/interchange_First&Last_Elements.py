list1=list(eval(input("Enter the elements = ")))
temp=list1[0]
list1[0]=list1[len(list1)-1]
list1[len(list1)-1]=temp
print(list1)
