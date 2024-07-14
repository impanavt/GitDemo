# class Parent:
#     def __init__(self):
#         self.__private_method()  # Call the private method
#
#     def __private_method(self):  # Private method using name mangling
#         print("This is a private method in the Parent class")
#
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()  # Call the Parent class constructor
#
#     def __private_method(self):  # Attempt to override the private method
#         print("This is an overridden private method in the Child class")
#
#
# # Create instances
# parent_obj = Parent()
# child_obj = Child()
#
#
# class Animal:
#     def sound(self):
#         return "Some generic animal sound"
#
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
#
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
#
# # Usage
# dog = Dog()
# cat = Cat()
# print(dog.sound())  # Output: Bark
# print(cat.sound())  # Output: Meow

# here Animal class a method 'sound'  .The 'Dog' and 'Cat' clas  overrides the method 'sound' to provide specific implementation

# Method Overloading
# Method overloading allows a class to have multiple methods with the same name, but with different parameters.
class MathOperations:
    def add(self, *args):
        return sum(args)

# Usage
math_ops = MathOperations()
print(math_ops.add(2, 3))          # Output: 5
print(math_ops.add(2, 3, 4))       # Output: 9
print(math_ops.add(1, 2, 3, 4, 5)) # Output: 15

