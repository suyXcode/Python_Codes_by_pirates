# constructor chaining by using super()
'''
class Demo:
    def __init__(self):
        print("This is Demo class constructor")


class Primary(Demo):
    def __init__(self):
        Demo.__init__(self)
        print("This is Primary class constructor")

ob1 = Primary()
'''
# constructor calling by using class
'''
class A:
    def __init__(self):
        print("This is the constructor of class A")

class B:
    def __init__(self):
        print("This is the constructor of class B")

class C:
    def __init__(self):
        print("This is the constructor of class C")

class Main(A,B,C):
    def __init__(self):
        C.__init__(self)
ob1 = Main()
'''

class Person:
    def __init__(self,a,b):
        self.name = a
        self.phno = b

class Qspider(Person):
    def __init__(self, a, b,c,d):
        super().__init__(a,b)
        self.email = c
        self.age = d
        
s1 = Qspider('x',987641234,'x@gmail.com',20)
print(s1.name)
print(s1.phno)
print(s1.email)
print(s1.age)