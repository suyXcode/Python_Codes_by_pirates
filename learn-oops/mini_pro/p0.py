from abc import ABC, abstractmethod

# 🔹 1. Abstraction
class Person(ABC):
    """Abstract class to define basic structure for a person"""
    
    @abstractmethod
    def show_details(self):
        pass


# 🔹 2. Encapsulation + Class Members + Object Members
class Student(Person):
    college_name = "KNIPSS College"  # class member (shared by all)

    def __init__(self, name, roll, marks):
        self.name = name                # object member (unique for each)
        self.roll = roll
        self.__marks = marks            # private variable (encapsulation)

    # Instance method → operates on object data
    def show_details(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.__marks}")

    # Getter and Setter (Encapsulation)
    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks! Must be between 0-100.")

    # Class Method → operates on class data
    @classmethod
    def get_college_name(cls):
        return cls.college_name

    # Static Method → Utility function
    @staticmethod
    def grade(marks):
        if marks >= 90:
            return "A+"
        elif marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"


# 🔹 3. Inheritance
class Topper(Student):
    def __init__(self, name, roll, marks, award):
        super().__init__(name, roll, marks)
        self.award = award

    # Method Overriding (Polymorphism)
    def show_details(self):
        print(f"🏅 Topper: {self.name}, Roll: {self.roll}, Marks: {self.get_marks()}, Award: {self.award}")


# 🔹 4. Demonstration
def main():
    print("🎓 WELCOME TO STUDENT MANAGEMENT SYSTEM 🎓\n")

    # Create objects
    s1 = Student("Suyash", 101, 88)
    s2 = Student("Aman", 102, 76)
    t1 = Topper("Riya", 103, 95, "Gold Medal")

    # Display details
    s1.show_details()
    s2.show_details()
    t1.show_details()  # overridden method

    print("\n🏫 College Name:", Student.get_college_name())

    # Encapsulation demo
    print("\nMarks before update:", s1.get_marks())
    s1.set_marks(92)
    print("Marks after update:", s1.get_marks())

    # Static method demo
    print("\nGrade of Suyash:", Student.grade(s1.get_marks()))
    print("Grade of Aman:", Student.grade(s2.get_marks()))

    # Polymorphism in action
    print("\n👩‍🏫 Displaying details using Polymorphism:")
    people = [s1, s2, t1]  # all are Person type
    for person in people:
        person.show_details()


if __name__ == "__main__":
    main()
