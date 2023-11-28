lst=list(eval(input("Enter the Elements = ")))
isTrue=False
for i in range(len(lst)):
    for j in range(len(lst)-1,-1,-1):
        if lst[i]==lst[j]:
            isTrue=True
        else:
            isTrue=False
if isTrue==True:
    print("Palindrome")
else:
    print("Not a Palindrome")