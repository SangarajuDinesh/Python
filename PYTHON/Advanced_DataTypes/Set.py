my_set1={1,2,3,4,5,'Dinesh',2+3j}
my_set2={2,3,5,7,9}
my_set1.add(10)
my_set1.update({2,3,4,5,6,7})
my_set1.pop()
my_set1.remove(6)
my_set1.discard(3)
print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))
print(my_set1.issubset(my_set2))
print(my_set1.issuperset(my_set2))
print(my_set1.difference(my_set2))
print(my_set1)