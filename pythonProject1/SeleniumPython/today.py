class calculator:
    num=100

    def __init__(self,a,b):
        self.first_number=a
        self.second_number=b
        print("I am called automatically whenever an object is created")

    def Summation(self):
     return self.first_number+self.second_number+self.num

obj=calculator(12,34)
print(obj.Summation())
