
'''
class Bank:
    __pin = '2025'
    def pin_check(self):
        pin = input("Enter the pin --")
        if pin == self.__pin:
            self.__withdrwal()
        else:
            print("Incorrect pin")

    def __withdrwal(self):
        print("Withdrawed successfully")

ob1 = Bank()
ob1.pin_check()
'''

'''
class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def get_salary(self):   # getter method --> used to access the private members
        return self.__salary
    
    def set_salary(self,sal): # setter method --> used to set the private members
        if sal >2000:
            self.__salary = sal
        

e1 = Employee(2000)    
print("Previous salary ---",e1.get_salary())
e1.set_salary(3000)
print("Updated salary ---",e1.get_salary())


print(e1.__salary)


class Circle:
    def __init__(self,radius):
        self.__radius = radius


    @property
    def radius(self):
        return self.__radius
    

    @property
    def area(self):
        return 3.1416*(self.__radius**2)
    
c1 = Circle(22)
print(c1.radius)
print(c1.area)
'''
class Person:
    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new):
        self.__name = new

    @name.deleter
    def name(self):
        del self.__name


ob1 = Person("Python")
print("Name is : ",ob1.name)
ob1.name = "Java"
print("Updated Name is : ",ob1.name)

print("Deleting the property name")
del ob1.name
print(ob1.name)