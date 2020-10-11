### argements
"""def sum(*args):
    s=0
    for i in args:
        s+=i # s=s+i
    print("sum is " ,s)

sum(10,20, 30 ,40)

def my_three(a,b,c,d):
    print(a,b,c,d)

args=[1,2,3,4]  # List

my_three(*args)"""

## key argements

def my_three(a,b,c):
    print(a,b,c)

a={'a': "one ", 'b': "two ",'c': "three"}

my_three(**a)

def myfunc(**kargs):
    for i,j in kargs.items():
        print(i,j)

myfunc(name ='tom',spot='football',rool='10',height='6.0')











