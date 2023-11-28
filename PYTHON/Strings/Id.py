name='Hello'
greet='world'
print(id(name[len(name)-1]))
print(id(greet[1]))
name1='Hello'
print(id(name))
print(id(name1))
if id(name)==id(name1):
    print('same')
else:
    print("not same")
if id(name[2])==id(greet[3]):
    print("same")
else:
    print("Not same")
if id(name1)==id(name):
    print("same")
else:
    print("Not same")
name2='kodnest'
name3='KODNEST'
name4=name3.lower()
if name2==name4:
    print("Same")
else:
    print("Not same")
if id(name2)==id(name4):
    print('same')
else:
    print("not same")