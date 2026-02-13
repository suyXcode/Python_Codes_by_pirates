#----------------
'''
class Math:

    def __init__(self):
        self.a = 10
        self.b = 20

    def add(self):
        print(self.a+self.b)
    addition = add # monkeypatching
    def add(self):
        print(self.a*self.b)
    product = add
    def add(self):
        print(self.a-self.b)

ob1 = Math()
ob1.addition()
ob1.product()


class Main:
    def greet(self,name = None):
        if name is not None:
            print(f"Hii {name}")
        else:
            print("Hello")

ob1 = Main()
ob1.greet()
ob1.greet("Nishant")


class Addition:
    def add(self,*args,**kwargs):
        print("This is addition method")
        print(sum(args))

ob1 = Addition()
ob1.add()
ob1.add(10,20)
ob1.add(1,2,3,4,5,6)

'''
#------------------------
# Method overriding
#------------------------

'''
class Parent:
    def marry(self):
        print("Marry to Simran ")

class Child(Parent):
    def marry(self):
        print(f"Marry to Rashmika ")

ob1 = Child()
ob1.marry()
    

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

'''
#------------------------
# Operator overloading
#------------------------

# Method overloading allows python 's built in operators to work on userdefined obejcts by defining the magicmethod/special methods inside the class

# Dunder method / magicmethods/ special methods

'''
class Arthmatic:
    def __init__(self,a):
        self.a = a

    def __add__(self,other):
        return self.a + other.a

    def __sub__(self,other):
        return other.a - self.a

ob1 = Arthmatic(10)
ob2 = Arthmatic(20)
print(ob1 + ob2)
print(ob1 - ob2)
'''
#------------------------
# Duck Typing
#------------------------
# walks like a duck , quacks like a duck


class Human:
    def sound(self):
        print("Human speaks")

class Duck:
    def sound(self):
        print("Duck quacks..!!")


ob1 =Human()
ob2 =Duck()
ob1.sound()
ob2.sound()


















