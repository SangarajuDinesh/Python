input1=input("Enter the String = ")
input2=input("Enter the Character to remove = ")
#----using logic-----
input3=""
for i in input1:
    if i!=input2:
        input3+=i
print(input3)

#-------Using replace() method-------
input4=input1.replace(input2,'')
print(input4)