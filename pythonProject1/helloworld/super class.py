# class SuperClass:
#     def some_method(self):
#         print("Superclass method")
#
# class SubClass(SuperClass):
#     def some_method(self):
#         super().some_method()  # Call superclass method
#         print("Subclass method")
#
# obj = SubClass()
# obj.some_method()

# to ccess the methods of super class use super()

# syntax
# class SuperClass:
#     pass
#
# class SubClass(SuperClass):
#     pass

# class SuperClass:
#     def __init__(self, x):
#         self.x = x
#
# class SubClass(SuperClass):
#     def __init__(self, x, y):
#         super().__init__(x)  # Initialize superclass attribute
#         self.y = y  # Initialize subclass attribute
#
# obj = SubClass(10, 20)
# print(obj.x)
# print(obj.y)


# multiple inheritance

# class Base1:
#     def some_method(self):
#         print("Base1 method")
#
# class Base2:
#     def some_method(self):
#         print("Base2 method")
#
# class SubClass(Base1, Base2):
#     def some_method(self):
#         super().some_method()  # Call method of Base1
#         print("Subclass method")
#
# obj = SubClass()
# obj.some_method()
#multi level inheritance
class Parent1:
   def parent1_func(self):
       print("Hi I am first Parent")

# Parent class2
class Parent2:
   def parent2_func(self):
       print("Hi I am second Parent")

# Child class
class Child(Parent1, Parent2):
   def child_func(self):
       super().parent1_func()
       self.parent2_func()

# Driver's code
obj1 = Child()
obj1.child_func()

# super() is particularly useful in multiple inheritance scenarios, where it helps to avoid calling the same method multiple times

# class A:
#     def say_hello(self):
#         print("Hello from A")
#
# class B(A):
#     def say_hello(self):
#         print("Hello from B")
#         super().say_hello()
#
# class C(A):
#     def say_hello(self):
#         print("Hello from C")
#         super().say_hello()
#
# class D(B, C):
#     def say_hello(self):
#         print("Hello from D")
#         super().say_hello()
#
# # Example usage
# d = D()
# d.say_hello()
# # Output:
# # Hello from D
# # Hello from B
# # Hello from C
# # Hello from A
