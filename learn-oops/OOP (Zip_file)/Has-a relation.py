#----------------
# Has-a relation
#----------------
# One class owns another clas / One class contains anotherclass

# Object of one class will be the property of another class
'''
class Address:
    def __init__(self,city,pin,phno,email):
        self.city = city
        self.pin = pin
        self.phno = phno
        self.email = email

class Personal_info:
    def __init__(self,age,gender):
        self.age = age
        self.gender = gender
        



class Customer:
    def __init__(self,name):
        self.name = name
        self.addr = Address('Noida',201301,876541,'a@gmail.com')
        self.info = Personal_info(20,'Male')

c1 = Customer('Akash')
print(c1.name)
print(c1.addr.city)
print(c1.addr.pin)
print(c1.addr.email)
print(c1.addr.phno)
print(c1.info.age)
print(c1.info.gender)


class Student:
    def __init__(self,name):
        self.name =name
        self.addr = Address('Delhi',200300,98765432,'s@gmail.com')
        self.info = Personal_info(18,"Male")
s1 = Student("Vivek")
print(s1.name)
print(s1.addr.city)
print(s1.addr.email)
print(s1.addr.pin)
print(s1.addr.phno)
print(s1.info.age)
print(s1.info.gender)

'''
#--------------
#Aggeregation
#--------------
'''
class Enginee:
    def start(self):
        print("Enginee is starting..!!")

class Car:
    def __init__(self,eng):
        self.enginee = eng

eng = Enginee()
car = Car(eng)
car.enginee.start()
'''
#--------------
# Composition
#--------------
class Enginee:
    def start(self):
        print("Enginee is starting..!!")

class Car:
    def __init__(self):
        self.enginee = Enginee()


car = Car()
car.enginee.start()






#Has -A relationship
#----------------------

# It is a type of relationship where one class contains another class (one class owns another class)
# where object of one class used as the property of another class


 # 2types of has-a relationship
 # Aggregation  (object is independent) ex- Teacher-student , Team-player
# composition   (Dependent)  ex-  car-Engine , House - Room






class Address:
    def __init__(self,city,pin,state):
        self.city = city
        self.pin = pin
        self.state = state
add = Address("Delhi",900,"Delhi")
class Customer:
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr

ob1 = Customer("Bobby",Address('Noida',754022,'UP'))

print(ob1.name)
print(ob1.addr.city)
print(ob1.addr.pin)
print(ob1.addr)


#------------------------
# Example (Aggregation)
#------------------------

class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine   # Car receives an existing Engine object

# Engine exists independently
engine = Engine()
car = Car(engine)

car.engine.start()

#Here:--
#Car has-a Engine, but the engine object was created outside the car.
#Even if the Car object is deleted, the engine object still exists.






#------------------------------
# Example (composition)
#------------------------------
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car creates the Engine internally

car = Car()
car.engine.start()

#Here:--
#Car creates the Engine.
#If the Car is destroyed, the engine has no existence.