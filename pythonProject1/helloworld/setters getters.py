class MyClass:
    def __init__(self, x):
        self._x = x  # Private attribute conventionally marked with a single underscore

    # Getter method for accessing the attribute value
    def get_x(self):
        return self._x

    # Setter method for modifying the attribute value
    def set_x(self, value):
        self._x = value

# Creating an instance of MyClass
obj = MyClass(10)

# Using the getter method to access the attribute value
print("Initial value of x:", obj.get_x())  # Output: Initial value of x: 10

# Using the setter method to modify the attribute value
obj.set_x(20)

# Using the getter method again to confirm the modification
print("Modified value of x:", obj.get_x())  # Output: Modified value of x: 20
