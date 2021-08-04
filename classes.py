#class programs
class a:
    def f(self):
        print("hello")
        
a1=a()
print(a1.f())

#
class d:
    a=4
    def __init__(self,a):
        self.a=a
        print(a)
    
    def f(this):
        print("hello")
d1=d(2)
print(d1.a)

#const
class d:
    a=8111
    def __init__(self,a):
        self.a=a
        print(a)
        
    def __init__(self,b):
        self.b=b
        print("this is 2nd const:",b)
    
    def f(self):
        print("hello")

d1=d(40)
print(d1.a)
print(d1.b)

#self
class a:
    def __init__(self):
        print("one")
    def __init__(self):
        print("two")
    def __init__(self):
        print("three")
        
print(a())

#_init_
class Person:
   
    # init method or constructor 
    def __init__(self, name):
        self.name = name
   
    # Sample Method 
    def say_hi(self):
        print('Hello, my name is', self.name)
   
p = Person('Vedant')
p.say_hi()

#
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"




person = Employee("robert", 255, "Instructor")

stark = Employee()
stark.name = "Rohan"
stark.salary = 4554
stark.role = "Student"

bruce = Programmer("bruce", 555, "Programmer", ["python"])