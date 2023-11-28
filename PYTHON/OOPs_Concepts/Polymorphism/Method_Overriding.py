class Calculator:
    def calculate(self):
        print("Calculator")
class Add(Calculator):
    def calculate(self,a,b):
        print(a+b)
class Sub(Calculator):
    def calculate(self,a,b):
        print(a-b)
class Mul(Calculator):
    def calculate(self,a,b):
        print(a*b)
a=int(input("Enter the First value = "))
b=int(input("Enter the second value = "))
c=Calculator()
c.calculate()
ad=Add()
ad.calculate(a,b)
su=Sub()
su.calculate(a,b)
mu=Mul()
mu.calculate(a,b)