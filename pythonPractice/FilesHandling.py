# Files write

"""file=open('D:\myfile.txt','w')  # open file for writing
file.write('This is first line\n')
file.write('This is second line\n')

file.close()"""

## Reading all the data at once.

"""file=open('D:\myfile.txt','r')
#print(file.read())  # read entire content of file at once
print(file.read(10)) # read given number of characters from as file
file.close()"""

"""file=open('D:\myfile.txt','r')
#print(file.readlines())  # read entire line  of file at once and array formate
print(file.readline())  # read the first line

# appending data

file=open('D:\myfile.txt','a')
file.write('This is third line\n')
file.close()"""

# Read the data for loop statement

file=open('D:\myfile.txt','r')

for l in file:
    print(l)
file.close()
