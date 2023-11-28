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
c=Calculator()
c.calculate()
a=Add()
b=Sub()
c=Mul()


x=int(input("Enter the first value = "))
y=int(input("Enter the second value = "))
class DuckTyping:
    def duck(self,x,a,b):
        if type(x).__name__=='Add':
            print("Addition should be perform")
        x.calculate(a,b)
d=DuckTyping()
d.duck(a,x,y)
d.duck(b,x,y)
d.duck(c,x,y)