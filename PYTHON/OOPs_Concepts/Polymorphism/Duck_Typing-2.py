class Calculator:
    def calculate(self):
        print("calculator")
class Add(Calculator):
    def calculate(self,x,y):
        print(x+y)
class Sub(Calculator):
    def calculate(self,x,y):
        print(x-y)
class Mul(Calculator):
    def calculate(self,x,y):
        print(x*y)
x=int(input("Enter the first value = "))
y=int(input('Enter the second value = '))
c=Calculator()
c.calculate()
a=Add()
b=Sub()
c=Mul()
def duck(a,x,y):
    a.calculate(x,y)
duck(a,x,y)
duck(b,x,y)
duck(c,x,y)
