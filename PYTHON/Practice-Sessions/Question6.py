n=input("Enter the String = ")
count=1
n=sorted(n)
print(n)
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        count+=1
    else:
        print(n[i]," occurs in ",count," times")
        count=1
    if i+1==len(n)-1:
        print(n[i+1],"occurs in ",count," times")

