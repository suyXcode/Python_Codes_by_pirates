class Student:
    student_count = 0

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student.student_count +=1
    
    def grade(self):
        if self.marks >= 90:
            grd = 'A'
        elif self.marks >= 70:
            grd = 'B'
        elif self.marks >= 60:
            grd = 'C'
        elif self.marks >= 40:
            grd = 'D'
        else:
            grd = 'F'
        print(grd)

    def student_info(self):
        print(f"Student name : {self.name}\nmarks: {self.marks}\nstatus : {self.pass_fail(self.marks)}")

    @classmethod
    def total_students(cls):
        print(f"Total no. of students : {cls.student_count}")

    @staticmethod
    def pass_fail(marks):
        if marks >=30:
            return "Pass"
        return "Fail"


s1 = Student('Akash',66)
s2 = Student('Dishu',38)
s3 = Student('Kashif',25)

s2.student_info()