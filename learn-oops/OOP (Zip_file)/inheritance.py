#---------------------------
# single level inheritance
#---------------------------
'''
class Main:
    a = 100
    b = "hello"
class Demo:
    a = 200
    b = "Bye"
class New(Demo):
    c= "This is child class"

ob1 = Main()
print(ob1.a)
print(ob1.b)
'''
#---------------------------
# multilevel inheritance
#---------------------------
'''
class First:
    a = 10
    b = 20

class Second(First):
    x= 'hii'
    y= 'Hello'

class Third(Second):
    j = True
    k = False

ob1 = Third()

print(ob1.a)
print(ob1.b)
print(ob1.x)
print(ob1.y)
print(ob1.j)
print(ob1.k)
'''
#---------------------------
# multiple inheritance
#---------------------------
'''
class Addition:
    @staticmethod
    def add(a,b):
        return a+b
class Substarction:
    @staticmethod
    def sub(a,b):
        return b-a
class Product:
    @staticmethod
    def pro(a,b):
        return a*b

class calculator(Addition,Substarction,Product):
    @staticmethod
    def div(a,b):
        return a/b

ob1 = calculator()
print(ob1.add(10,20))
print(ob1.sub(10,20))
print(ob1.pro(10,20))
print(ob1.div(10,20))



# Method Resolution Order (MRO)
class A:
    x = 0
    y = 20
class B:
    x = False
    y = "Hii"
class C:
    x = "Red flag"
    y = "Green flag"

class Child(B,C,A):
   pass
ob1 = Child()
print(ob1.x)
print(ob1.y)

'''

#---------------------------
# Hierarchecal inheritance
#---------------------------

'''
class Parent:
    s  = "This is parent class"

class A(Parent):
    a = "Hii"

class B(Parent):
    b = "Hello"

ob1 = A()
ob2 = B()

print(ob1.s)
print(ob1.a)

print(ob2.s)
print(ob2.b)

'''
#---------------------------
# Hybrid inheritance
#---------------------------

class Upper:
    @staticmethod
    def uppercase():
        res = ''
        for i in range(ord('A'),ord('Z')+1):
            res += chr(i)
        return res

class Alpha(Upper):
    @staticmethod
    def lowercase():
        res = ''
        for i in range(ord('a'),ord('z')+1):
            res += chr(i)
        return res

class Numbers:
    @staticmethod
    def digits():
        res = ''
        for i in range(10):
            res += str(i)
        return res
    

class Characters(Alpha,Numbers):
    @staticmethod
    def special_chars():
        res = ''
        for i in range(33,127):
            if not(chr(i).isalnum()):
                res += chr(i)
        return res
    
ob1 = Characters()
print(ob1.uppercase())
print(ob1.lowercase())
print(ob1.digits())
print(ob1.special_chars())
    
