# Public -Public Members: Accessible from anywhere. No special naming convention.

class MyClass:
    def __init__(self):
        self.public_var = "I am a public variable"

    def public_method(self):
        return "I am a public method"

# Usage
obj = MyClass()
print(obj.public_var)           # Accessing public variable
print(obj.public_method())      # Accessing public method


# protected -Protected Members: Intended for internal use within the class and its subclasses. Indicated by a single underscore _.

class MyClass:
    def __init__(self):
        self._protected_var = "I am a protected variable"

    def _protected_method(self):
        return "I am a protected method"

class SubClass(MyClass):
    def access_protected(self):
        return self._protected_var, self._protected_method()

# Usage
obj = SubClass()
print(obj.access_protected())   # Accessing protected members from subclass
print(obj._protected_var)       # Accessing protected variable (not recommended)



# privtae-Private Members: Intended for internal use within the class only. Indicated by a double underscore __, which triggers name mangling.

class MyClass:
    def __init__(self):
        self.__private_var = "I am a private variable"

    def __private_method(self):
        return "I am a private method"

    def access_private(self):
        return self.__private_var, self.__private_method()

# Usage
obj = MyClass()
print(obj.access_private())     # Accessing private members through a public method

# Attempting to access private members directly will result in an attribute error
try:
    print(obj.__private_var)
except AttributeError as e:
    print(e)  # 'MyClass' object has no attribute '__private_var'



