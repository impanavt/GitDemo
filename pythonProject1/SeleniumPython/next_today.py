from today import calculator

class childImpp(calculator):
    num2=200

    def __init__(self):
        calculator.__init__(self,23,45)

    def getCompleteData(self):
        Summ=self.Summation if self.Summation is not None else 0
        return self.num2

obj=childImpp()
print(obj.getCompleteData())