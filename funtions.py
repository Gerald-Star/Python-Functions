
# * Python List
primeNumbers = [2,3, 4, 5, 6, 7]
print(primeNumbers[2])

bestPrime = primeNumbers[5]
print(bestPrime)

primeNumbers.append(12)
print(primeNumbers)

primeNumbers.remove(4)
print(primeNumbers)

# * Tuples in Python and Use cases
# What is a Tuple?
# A tuple is a collection of objects , which is in ordr and immutable
# Elements inside a tuple cannot be changed once they are assigned
#Tuples are used to store multiple itzems in a single variable

# Different between Tuple and Python list

# A tuple is created by placing thje elements in a bracket, 
# can contain different types of elements
tuple1 = (3, 5, 4, 4, 7, 6, "soflife", 4.8)
print(tuple1)
print(type(tuple1))
print(tuple1[3])

# dot notation and bracket notation in tuple
print(tuple1.index(3)) # use the index function to find the particular position of an element
print(tuple1.index(5))
print(tuple1.count(4)) # number of times an element appears

# tupleToList
tupleToList = list(tuple1)
print(tupleToList) # to list all the element use list()
print(type(tupleToList )) # a class list

# change a data type into tuple
num = [1, 2, 4]#
listTuple = tuple(num)
print(listTuple)
print(type(listTuple))


# how to use .partition
txt = 'I could eat bananas all day'
x = txt.partition('apples')
print(x)