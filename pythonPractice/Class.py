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

"""class MyClass:
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
print(c1 is not c3)"""

### Creating Constructor

"""class MyClass:
    def m1(self):
        print("good morning")
    def __init__(self):
        print("this i constructor")

c=MyClass()
c.m1()"""

#### Converting local variables into class variables

"""class MyClass:
    def values(self,val1,val2):  # val1 & val2 are local variable
        print(val1)  # here local variable 10
        print(val2)   # here local variable 10
        self.val1=val1
        self.val2=val2

    def add(self):
         print(self.val1+self.val2)   # here class variable 30

mc=MyClass()
mc.values(10,20)
mc.add()

## Converting local variables into class variables  Constructor

class MyClass:
    def __init__(self,val1,val2):  # val1 & val2 are local variable
        print(val1)  # here local variable 10
        print(val2)   # here local variable 10
        self.val1=val1
        self.val2=val2

    def add(self):
         print(self.val1+self.val2)   # here class variable 30

mc=MyClass(100,200)
mc.add()"""

## how to call current class method in another metod

"""class MyClass:
    def m1(self):
        print("this is m1 method")
        self.m2(100)

    def m2(self,a):
        print("this is m2 method",a)

c1=MyClass()
c1.m1()"""

## Constructor with arguments

"""class MyClass:
    name ="Kumar"
    def __init__(self,name):
        print(name)  # Constructor argument local
        print(self.name) # represent class variables

c=MyClass("pavan")

# another example

class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def display(self):
        print("Empid: {}  EmpName :{} Empsal: {} " .format(self.eid,self.ename,self.esal))
        print("Empid: %d  EmpName : %s Empsal: %g " % (self.eid, self.ename, self.esal))

el=Emp(101,'venki',85000)
el.display() """

### __str__

"""class MyClass:
    pass
c = MyClass() # c is the reference variable 
print(c)   # <__main__.MyClass object at 0x0000000002519370>

class MyClass:
    def __str__(self):
        return "Welcome"  # allow only string value 

c=MyClass() # c is the reference variable 
print(c)    # <__main__.MyClass object at 0x0000000002519370> welcome  """

"""class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def __str__(self):
        return ("Empid: {}  EmpName :{} Empsal: {} " .format(self.eid,self.ename,self.esal))


el=Emp(101,'venki',85000)
print(el) """


## __del__

"""class MyClass:
    def __del__(self):
        print("Destroyed")

c1=MyClass()
c2=MyClass()

del c1 """






































