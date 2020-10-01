"""def sum():
    x=10
    y=20
    z=x+y
    print(z)

sum()"""

"""def sum(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
        print(result)

sum(10,20)"""

"""def sum(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
    return result

s=sum(10,20)
print(s)"""

"""def sum(start, end):
    if(start >end):
        print("start should be less than end")
        return # None
    result=0
    for i in range (start,end+1):
        result=result+i
    return result
s=sum(1,5)
print(s)"""

# Local & Global variables

"""global_var=12  # a global variable -- out side function

def func():
    local_var = 100   # this is local variable -- in side function
    print(global_var)  # you can access global variables in side function
    print(local_var)

func()

print(local_var)  # name error :name "local_var" is not defined """

"""xy =100

def cool():
    xy=200
    print(xy)
cool()  #200

print(xy)  #100 """

## anythor example

"""t=1

def increment():
    # global t=10 # incorrect
    global  t
    t=100
    print(t)  #100

increment()

print(t)  # 100"""

## Paasing arguments values

# Passing Arguments with default values (positions)

"""def func(i,j=100):
    print(i,j)

func(50) # 50 100

func(50,250)  # 50 , 250


def named_args(name,greeting):
    print(greeting + " " +name)

named_args("pavan" , "Hi")  # Positional Arguments

named_args(name='venki',greeting="hi")  # Keyword Arguments
named_args(greeting='hi',name="ram")  # Keyword Arguments """

def my_func(a,b,c):
    print(a,b,c)

my_func(10,20,30) # 10 ,20, 30 Positional arguments

my_func(10,b=20,c=30) # 10 ,20, 30 Positional arguments & Key worf arguments

my_func(10,c=30,b=30) # 10 ,20, 30 Positional arguments & Key worf arguments

#my_func(10,b=20,30) # incorrect positional argument must apper before any keyword argument


## Returning multiple values from function ## -->Multiple values are returned as tuples

def bigger(a,b):
    if a>b:
        return a,b
    else:
        return b,a

s=bigger(100,200)
print(s)










