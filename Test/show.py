class Show:
    def __init__(self,name,age):
        self.__name=name
        self.age=age

    def showq(self):
        print(self.__name,self.age)
    def getName(self):
        return self.__name
p=Show("holiday",22)
# print(p.getName())
p.showq()