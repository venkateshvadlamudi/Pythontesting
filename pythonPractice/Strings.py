# Creating strings

# Approach 1

# name ="john"
name ='john'
print(name)

# Approach 2
name1=str("welcome")
print(name1)

# string Id value Immutable

str1="welcome"
str2="welcome"

print(id(str1))  # 38958064   string value
print(id(str2))   # 38958064

str2=str2+"to python"
print(id(str1))  # 38958064
print(id(str2))   #38891152

# string operations  " + * "

str="welcome"

print(str+"to programming")

print(str *10)

# slicing

str ="welcome"

print(str[1:3])
print(str[:6])
print(str[3:5])
print(str[3:])


# string Functions

str ="Welcome"

print(len(str))
print(max(str))
print(min(str))

# strings "in & not in functions"

str="welcome"
print("wel" in str)
print ("xyz" in str)

print("wel" not in str)
print ("xyz" not in str)

#String Comparision

print("tim" == "tie")  # False
print("free" != "freedom") # True
print("arrow" > "aron")  # true
print("Right" == "left") # True
print("teeth" == "tee")  # False
print("yellow" <= "fellow") # false
print("abc" > "") # True

# ittreative strings

s="python"
for i in s:
    print(i)
    print(s ,end="\n")
    print(s, end="")
    print(s,end="foo")


s = "python"
for i in s:
     print(s)

# Testing string

s="welcome to python"

print(s.isalnum()) # False
print("welcome".isalpha()) # true
print("2020".isdigit()) # True
print("first Number".isidentifier()) # false
print(s.islower()) # True
print("WELCOME".isupper()) #True
print("".isspace()) # True

#Searching for substring

s= "welcome to python"

print(s.endswith("thon")) # true
print(s.startswith("good")) # False

print(s.find("come"))
print(s.find("become"))
print(s.rfind("o"))
print(s.count("o"))

# Converting Strings

s="String in PYTHON"

s1=s.capitalize()
print(s1)

s2=s.title()
print(s2)

s3=s.lower()
print(s3)

s4=s.upper()
print(s4)

s5=s.swapcase()
print(s5)

s6=s.replace("in", "on")
print(s6)

print(s)
