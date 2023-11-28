class Demo:
    @staticmethod
    def disp():
        Demo.x=10
Demo.disp()
print(Demo.x)

#**************************
class Demo1:
    age=22
    def __init__(self):
        self.x=10
        Demo1.y=20
    @staticmethod
    def disp():
        Demo1.z=20
print(Demo1.age)
d=Demo1()
print(d.y) #Accesing static variable using reference
print(Demo1.y)
Demo1.disp()
print(Demo1.z)