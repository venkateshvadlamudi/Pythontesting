t1=()  # Creates an empty tuple with no data
t2=(11,22,33)
t3=tuple([1,2,3,4,5]) # tuple from array
t4=tuple("abcd")  # tuple from string

print(t1)
print(t2)
print(t3)
print(t4)

# Tuples Functions
t1= (1,2,12,34,54,76,98)

print(min(t1))
print(max(t1))
print(sum(t1))
print(len(t1))

# Iterating through tuples --> Tuples are iterable using for loop

for i in t1:
    print(i,end=" ")

# Slicing Tuples
t= (1,2,12,34,54,76,98)
print(t[0:3])
print(t[2:4])

# in and not in operator

t= (1,2,12,34,54,76,98)
print(12 in t)
print(12 not in t)
