# private variable can be access only within the method

"""class myClass:
    __a=10
    def display(self):
        print(self.__a)

obj=myClass()
obj.display()


print(myClass.__a)  # we cannot access bcoz it is private variable
"""

# private method can be access only within the method

class myClass:
    def __display1(self):
        print("this is display 1 method ")

    def display2(self):
        print("This is dispaly method 2")
        self.__display1()


obj=myClass()
#obj.__display1()  # not correct
obj.display2()

# we can access private variable outside of class indirectly using method

class myClass:
    __empid=101

    def getempid(self,eid):
        self.__empid=eid

    def dispalyid(self):
        print(self.__empid)

obj=myClass()

obj.getempid(106)

obj.dispalyid()













