from HelloWorld import Selenium


class ChildImp(Selenium):
    num1 = 100

    def __init__(self):
        Selenium.__init__(self, 2, 10)


    def getCompleteData(self):
        return self.num1 + self.num + self.Summation()


obj = ChildImp()
print(obj.getCompleteData())