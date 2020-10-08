## Single Inheritance

"""class A:
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")

aobj=A()
aobj.m1()

bobj=B()
bobj.m1()  #A
bobj.m2() # B """

"""class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

b=B()
b.m1()
b.m2()"""

## Multi level  Inheritance

"""class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

class C(B):
    i,j=1,2
    def m3(self):
        print(self.i+self.j)

b=B()
b.m1()
b.m2()

c=C()
c.m1()
c.m2()
c.m3() """

## HIERARCHICAL  Inheritance

"""class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

class C(A):
    i,j=1,2
    def m3(self):
        print(self.i+self.j)

b=B()
b.m1()
b.m2()

c=C()
c.m1()
c.m3() """

## Multiple  Inheritance

"""class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B:
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

class C(A,B):
    i,j=1,2
    def m3(self):
        print(self.i+self.j)


c=C()
c.m1()
c.m2()
c.m3() """

## Super() class keyword using
## to invoke parent class methods

"""class A:
    def m1(self):
        print("This is method from A")

class B(A):
    def m2(self):
        print("This is method from B")
        super().m1() # calling parent  class method using super()

b=B()
b.m2() """

### To invoke parent class variables

"""a,b=10,15

class A:
    a,b=10,20

class B(A):
    a,b= 100,200
    def m1(self,a,b):
        print(a+b)   #local variables
        print(self.a+self.b)  # Child class variables
        print(super().a+super().b) # Parent class variables
        print(globals()['a']+globals()['b'])

bobj=B()
bobj.m1(1,2) """

### To invoke parent class constructor

"""class A:
    def __init__(self):
        print("constructor from A")

class B(A):
    pass

bobj=B()  """


"""class A:
    def __init__(self):
        print("constructor from A")

class B(A):
    def __init__(self):
        print("constructor from B")
        # super().__init__() # Appraochi1 # calla parent class constructor
        A.__init__(self)  # Appraochi2 # calla parent class constructor

bobj=B() """


