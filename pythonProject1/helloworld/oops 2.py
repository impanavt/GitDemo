from oops import calculator
# inheritance is determined by the childImp inheriting from the class calculator
class childImp(calculator):
  num2=200

  # init -to initialie objects created from parent class-constructor method
  def __init__(self):
    # to initialie attributes inherited from parent class or super class calculator
    calculator.__init__(self,2,10)
  # polymorphism getData() and summation() methods which are inherited from the calculator class and overridden in the childImp class.
  # This allows for code reuse and flexibility, as the same method can operate on objects of different classes
  def getCompleteData(self):
    data = self.getData() if self.getData() is not None else 0
    summ = self.summation() if self.summation() is not None else 0
    return self.num2
#   the child class inherits attributes num ,and methods getData() ,Summation() from parent class


obj=childImp()
print(obj.getCompleteData())


# encapsulation is demonstrated by use of classes calculator ,childImp to encapsulate attributes and methods within object
# Acceess to attributes num2 ,num ,first_number ,second_number is controlled through methods getData() and summation() allowing for data hiding

# Abstraction is achieved through method abstraction,
# where the internal implementation details of methods (getData() and summation()) are hidden from the user of the class.



