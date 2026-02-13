# Constructor
'''
class School:
    def __init__(self,a,b,c):
        self.sname = a
        self.addr = b
        self.phno = c

ob1 = School("Jitu",'somewhere','1111111')
ob1 = School("Jitu",'somewhere','1111111')
ob1 = School("Jitu",'somewhere','1111111')
ob1 = School("Jitu",'somewhere','1111111')

print(ob1.sname)
print(ob1.addr)
print(ob1.phno)
'''

class Employee:
    a = 10
    def __init__(self,eid,ename,phno,salary,addr):
        self.eid = eid
        self.ename = ename
        self.phno = phno
        self.salary = salary
        self.addr = addr
        # print(f"Employee with name {self.ename} is registred successfully..")

e1 = Employee("E001","Saurabh",99888777,20000,"Delhi")
e2 = Employee("E002","Nishant",7008357193,25000,"Noida")
e3 = Employee("E003","Raghav",9668816201,30000,"Faridabad")

'''
emp_list = [e1,e2,e3]
for emp in emp_list:
    print(f"Employee name {emp.ename}\nEmployee addressn{emp.addr}")
    print("="*30)

def show_details(emp):
    print(emp.ename,emp.salary)

show_details(e1)
show_details(e2)
show_details(e3)
'''

class CarShowroom:
    pass

class Employee:
    pass

class Bank:
    pass