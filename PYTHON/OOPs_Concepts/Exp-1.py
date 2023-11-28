class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self):
        print(self.name,"Is working")
    def play(self):
        print(self.name," is playing")
emp1=Employee('Akash',34,35000)
print(emp1.name,emp1.age,emp1.salary)
emp1.work()
emp1.play()
emp2=Employee('Neha',29,45000)
print(emp2.name,emp2.age,emp2.salary)
emp2.work()
emp2.play()
