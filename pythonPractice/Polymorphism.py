# Overriding a variable

"""class Parent:
    name ="scott"

class Child(Parent):
    name="David"

obj=Child()
print(obj.name)  # David

# Overriding a Methods

class Bank:
    def ratofinterest(self):
        return 0

class ICICI(Bank):
    def ratofinterest(self):
        return 10.5

obj=ICICI()
print(obj.ratofinterest())

obj1=Bank()
obj1.ratofinterest()

# Overloading Methods

class Human:
    def sayHellow(self,name=None):
        if name is not None:
            print("Hello  "+name)
        else:
            print("Hello")

obj=Human()
obj.sayHellow("Venki")
obj.sayHellow() """

class Bird:
    def fly(self,name=None):
        if name=="parot":
           print("Can fly")
        if name=="penduine":
            print("cannot fly")
        if name is None:
            print("No input")

obj=Bird()
obj.fly("parot")
obj.fly("penduine")
obj.fly()



