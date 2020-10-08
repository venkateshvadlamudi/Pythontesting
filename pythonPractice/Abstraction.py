# ABC is pre defined abstract class

from abc import ABC,abstractmethod

"""class A(ABC):
    @abstractmethod
    def display(self):
        None

class B(A):
    def display(self):
        print("this is display method")

obj=B()
obj.display() """

"""class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("eat NON-VEG")

class Cow(Animal):
    def eat(self):
        print("eat VEG")


t=Tiger()
t.eat()

c=Cow()
c.eat() """

"""class X(ABC):
    @abstractmethod
    def m1(selfs):
        pass
    @abstractmethod
    def m2(self):
        pass

class Y(X):
    def m1(selfs):
        print("This is m1")

class Z(Y):
    def m2(self):
        print("This is m2")

zobj=Z()
zobj.m1()
zobj.m2() """

class Cal(ABC):
    def __init__(self,value):
        self.value=value
        @abstractmethod
        def add(self):
            pass
        @abstractmethod
        def sub(self):
            pass

class C(Cal):
    def add(self):
        print(self.value+100)

    def sub(self):
         print(self.value-10)

cobj=C(100)
cobj.add()
cobj.sub()






