"""class Myclass:  # Creating Class
    def myfunc(self):
        pass

    def display(self, name):
        print("Name is :" , name)


        # Function . # Method  --> in python function and class both are same...

        # Function --> creating function out side class
        # method  --> creating in side class
mc=Myclass()
mc.myfunc()
mc.display("venki") """

## Instance method & Static method ##

"""class MyClass:
    def m1(self):   # instance Method
        print("Instance Method")

    @staticmethod
    def m2():
        print("static Method")

mc=MyClass()
mc.m1()   # instance method call object using

MyClass.m2()  # static method call direct class """

"""class MyClass:
    def m1(self):   # instance Method
        print("Instance Method")

    @staticmethod
    def m2(self):
        print("static Method")

mc=MyClass()
mc.m1()
MyClass.m2(10)
 """
# Declaring varaible inside the class

"""class MyClass:
    a,b=100,200 # class variables

    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=MyClass()

mc.add()
mc.mul()

### Local Variable , class variable  & Global Variables

i,j = 15,25  # Global Variables

class MyClass:
    a,b,=10,20  # Class Variables

    def add(self,x,y):   # local Variables
        print(x+y)    # accessing local variables
        print(self.a+self.b)  # accing class variables
        print(i+j)  # accing Global variable

mc=MyClass()
mc.add(100,200)"""

### Local Variable , class variable  & Global Variables with same variables

"""a,b = 15,25  # Global Variables

class MyClass:
    a,b,=10,20  # Class Variables

    def add(self,a,b):   # local Variables
        print(a+b)    # accessing local variables
        print(self.a+self.b)  # accing class variables
        print(globals()['a'] +globals()['b'])  # accing Global variable

mc=MyClass()
mc.add(100,200) """

## Creating multiple objects for one class

class MyClass:
    def display(self):
        print("Good morning")

obj1=MyClass()
obj1.display()


obj2=MyClass()
obj2.display()

# Named object & Nameless object

class MyClass:
    def display(self):
        print("Good morning")

obj1=MyClass()  # Named Object
obj1.display()

MyClass().display()  # Name less object

## How to check memory locations of object

class Myclass:
    def m1(self):
        pass

c1=MyClass()
c2=MyClass()
c3=c1

print(id(c1)) # 31819952
print(id(c2))  # 32084320
print(id(c3))  # 31819952

print(c1 is c2)  # False
print(c1 is c3)  # True

print(c1 is not c2)
print(c1 is not c3)












