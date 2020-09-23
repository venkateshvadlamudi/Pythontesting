
# if .. else

# Case 1 :

a= 30
if a>20:
    print("true conduction")
else:
    print("false conduction")

# Case 2 :

if True:
    print("true conduction")
else:
    print("false conduction")

# Case 3 :

if True:
    print("true conduction")
else:
    print("false conduction")

# Case 4 :
a=10
if a % 2 == 0:
    print("Even Number")
else:
    print(" odd  Number")


# Multiple statements under if block

if False:
    print("Statement1")
    print("Statement2")
    print("Statement3")
else:
    print("Statement4")
    print("Statement5")

print("Statement6")  # separate statement

# Single Line

print("welcome") if True else print("Python")
print("welcome") if False else print("Python")

print("welcome") if 20>10 else print("Python")
print("welcome") if 20<10 else print("Python")

# Multiple statements in Single Line

{print("welcome"),print("Python") if True else print("Python"),print("Welcome" )}
{print("Python"),print("welcome") if False else print("welcome"),print("Python...")}

# elif

a=50
if a==10:
    print("Ten")
elif a==20:
    print("Twenty")
elif a==30:
    print("Thirty")
else:  # optional
    print("Not Listed")