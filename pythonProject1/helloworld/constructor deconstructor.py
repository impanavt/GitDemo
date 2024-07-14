class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} is being destroyed")

    # destructor __del__

obj = MyClass("Example")
del obj  # The __del__() method is called automatically when obj is deleted


# class MyClass:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# obj = MyClass(10, 20)  # The __init__() method is called automatically when creating
# print(obj.x)

# Constructor
