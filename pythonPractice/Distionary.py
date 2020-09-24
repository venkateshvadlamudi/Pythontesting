# Creating Distionary

friends= {'tom': '123-123-1234' ,
          'jerry' : '456-789-7854'}

print(friends)

# retrieving
friends= {'tom': '123-123-1234' ,
          'jerry' : '456-789-7854'}

print(friends)

#Retrieving element from the distionary
print(friends['tom'])

#Adding elements into the distionary

friends['bob']='888-999-666'
print(friends)

#Modify elements into the distionary
friends['bob']='888-999-777'
print(friends)

# delete element from the distionary
del friends['bob']
print(friends)

# Looping items in the distionary

friends={'a': '100',
         'b' : '200',
         'c': '300',
         'd': '400'
         }
for x in friends:
    print(x ,":" , friends[x])

## Find the lenth of the distionary
print(len(friends))

## Equality Tests in distionary --> < ,> <=,<= can not use equality


d1={"miske" : 41 , "bob" : 3 }
d2={"bob" : 3  ,"miske" : 41  }

print(d1==d2)
print(d1 != d2)


friends= {'tom': '123-123-1234' ,
          'bob':'888-999-666',
          'jerry' : '456-789-7854'}

#popitem() --> Returns randomly select item from distionary and also remove the selected item

print(friends.popitem())

#Clear () Delete everything from distionary
print(friends.clear())

friends= {'tom': '123-123-1234' ,
          'bob':'888-999-666',
          'jerry' : '456-789-7854'}

#keys() Return  keys in distionary as tuple

print(friends.keys())

# Values()
print(friends.values())

#get(key)

print(friends.get('tom'))

#pop(key)

print(friends.pop('bob'))
print(friends)



















