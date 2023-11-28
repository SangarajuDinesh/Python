class Demo:
    def __init__(self):
        self.x=10
        self.name="Dinesh"
    def disp(self):
        print("Inside disp() method")
    def __str__(self):
        return str(self.x)
d1=Demo()
print(d1)