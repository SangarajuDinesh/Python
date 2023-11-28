lst1=list(eval(input("Enter the Elements for List1 = ")))
lst2=list(eval(input("Enter the Elements for List2 = ")))
lst3=[]
for i in range(len(lst1)):
    lst3.append(lst1[i])
for i in range(len(lst1),len(lst2)+len(lst1),1):
    lst3.append(lst2[i-len(lst2)])
print(lst3)
