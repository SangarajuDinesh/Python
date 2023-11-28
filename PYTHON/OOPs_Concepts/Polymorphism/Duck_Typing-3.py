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

def main():
    x=int(input("Enter the first value = "))
    y=int(input("Enter the second value = "))
    def duck(a,x,y):
        a.calculate(x,y)
    duck(Add(),x,y)
    duck(Sub(),x,y)
    duck(Mul(),x,y)
    Calculator().calculate()
main()