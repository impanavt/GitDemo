class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Department: {self.department}")

class Developer(Employee):
    def __init__(self, name):
        super().__init__(name, "Development")

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, "Management")

class SalesExecutive(Employee):
    def __init__(self, name):
        super().__init__(name, "Sales")

# Create instances of different types of employees
dev1 = Developer("John Doe")
manager1 = Manager("Jane Smith")
sales_executive1 = SalesExecutive("Alice Johnson")

# Display information about each employee
dev1.display_info()  # Output: Name: John Doe, Department: Development
manager1.display_info()  # Output: Name: Jane Smith, Department: Management
sales_executive1.display_info()  # Output: Name: Alice Johnson, Department: Sales
