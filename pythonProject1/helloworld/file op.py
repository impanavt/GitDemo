# class Details:
#     name='impana'
#     age=20
#
#     def sub(self):
#         print("My name is", self.name and " I am " , self.age , "years old")
#
# obj1=Details()
# print(obj1.name)
# obj1.sub()

# def my_decorator(func):
#     def wrapper():
#         print("something is happening before the function is called")
#         func()
#         print("something is happening after the function is called")
#     return wrapper
#
#
# @my_decorator
# def say_hello():
#     print("hello")
# say_hello()
#

# class Employee:
#   def __init__(self, name, id):
#     self.name = name
#     self.id = id
#
#   def showDetails(self):
#     print(f"The name of Employee: {self.id} is {self.name}")
#
# class Programmer(Employee):
#   def showLanguage(self):
#     print("The default langauge is Python")
#
#
# e1 = Employee("Rohan Das", 400)
# e1.showDetails()
# e2 = Programmer("Harry", 4100)
# e2.showDetails()
# e2.showLanguage()



class employee:

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetails(self):
        print(f"the name of the Employee : {self.id} is {self.name}")


class Program(employee):
    def showlanguage(self):
        print("python is my favourite language")

e1=employee("impana",67)
e1.showdetails()
e2=Program('thopes',89)
e2.showdetails()
e2.showlanguage()
