"""print("Program is started")

print(10/0)  # Zero Divisio Error

print("Program is Completed")
"""

"""print("Program is started")

try:
    print(10/0)  # Zero Divisio Error:
except ZeroDivisionError:
    print("Entered in to except block -handled exception")

print("Program is Completed")"""


"""print("Program is started")

try:
    print(10/5)  
except ZeroDivisionError:
    print("Entered in to except block -handled exception")

print("Program is Completed")"""


"""print("Program is started")

try:
    print(10/0)  
except TypeError:
    print("Entered in to except block -handled TypeError")
except ZeroDivisionError:
    print("Entered in to except block -handled ZeroDivisionError")

else:
    print("entered in to the else black ")

print("Program is Completed")"""

"""print("Program is started")

try:
    print(10 / 5)
except TypeError:
    print("Entered in to except block -handled TypeError")
except ZeroDivisionError:
    print("Entered in to except block -handled ZeroDivisionError")

else:
    print("entered in to the else black ")

print("Program is Completed") """

# Case1 : Thrown exception---> Except

# case 2 : Not Thrown expection ---> else (executed only if the statement not thrown any exception)

"""print("Program is started")

try:
    #print(10 /0)
    print(10 / 2)
except TypeError:
    print("Entered in to except block -handled TypeError")
except ZeroDivisionError:
    print("Entered in to except block -handled ZeroDivisionError")
else:
    print("entered in to the else black ")
finally:
      print("Entered in to finalily block ")

print("Program is Completed")"""

#Case 1: Exception occured ---> expect ---> finally
#Case 2: Exception occured --->Not Handled   --->  finally
#Case 3: Exception Not occured --->No  expect ---> else ---> Finally

### Raise Exception

"""def enterage(age):
    if age <0:
        raise ValueError("Only positive integer are allowed ")

    if age %2 == 0:
        print("age is even")
    else:
        print("age is odd")

try:
    #num=5
    #num=6
    num=-5
    enterage(num)
except ValueError:
    print("only positive integers are allowed ")
except:
    print("Something is wrong")"""


# Eception Objects

try:
    number=one
    print("This number is ", number)
except NameError as ex:
    print("Exception :", ex)















