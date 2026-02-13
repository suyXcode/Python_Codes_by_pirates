class Person:
    def __init__(self):
        self.name = None
        self.age = None

    def person_name(self):
        self.name = input("Enter your name :  ")
        return self
    def person_age(self):
        self.age = int(input("Enter the age : "))
        return self
    def show(self):
        print(f"Name of the person : {self.name}\nAge is {self.age}")
        return self
ob1 = Person()
ob1.person_name().person_age().show()  #method chaining


    
        