class calculator:
    num=100

    def __init__(self,a,b):
        self.first_number=a
        self.second_number=b
        print("I am called automatically ehenver an object is called")


    def getData(self):
        print("I m not execuring as method in python")


    def summation(self):
        return self.first_number+self.second_number+self.num


obj=calculator(2,3)
# obj.getData()
print(obj.summation())

# obj=calculator(10,15)
# obj.getData()
# print(obj.summation())
