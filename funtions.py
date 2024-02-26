# what is indentation in Python

# comments - single line comments
'''
double line or multiline comments
'''


# FUNCTIONS IN PYTHON; Methods and Procedures

# ! Functions with NO INPUT AND OUPUT
'''
def get_milk(money):
'''

'''
def get_milk(money):
liters = money / 2   # ! with Inputs, No outputs
'''


'''
def get_milk(money):
litres = money / 2
return litres   #! with inputs, with outputs

'''
def get_milk():  # function declaration
    print("Open the store\n walk to the shop")
    print("buy a milk")
    print("come home with the milk ")


get_milk()  # calling the function

print()
# ? Uing the f string to set the arguement


# parameter is the input to a function as a placeholder
def get_foodstuff(number, destination, amount):
    print('How much foodstuffs to buy')
    print(f'Make a list of {number} items')
    print(f'Take a taxi to the {destination}')
    print(f'Buy {amount} kilos of beans')
    print('return home on time')


get_foodstuff(10, 'Accra Mall', 20)

print()

# ? Parameters and Arguments in Function


# * Function Return Statement
# mechanics of returning values using the keyword return
# when a value returns a function, we store that value in a variable

tuple2 = (5, 10, 'softlinks', 8)
index = tuple2.index(8)

'''
create a function called times in python; 
have the function takes two inputs; 
multiply these inputs together; 
provide the result as an output
'''
def times(num1, num2):
    """
    Multiply two numbers together.

    Parameters:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float: The result of multiplying num1 and num2.
    """
    return num1 * num2

# Example result usage:
result = times(3, 4)
print(result)  # Output will be 12


# ? Example

def student_scores(text, exam):
  # total_scores = text + exam 
  # return total_scores (MAKE A SINGLE LINE)
  return text + exam

grade = student_scores(30, 70)
print(grade)





print()
# * Python List
primeNumbers = [2, 3, 4, 5, 6, 7]
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
# Tuples are used to store multiple itzems in a single variable

# ? Different between Tuple and Python list

# A tuple is created by placing thje elements in a bracket,
# can contain different types of elements
tuple1 = (3, 5, 4, 4, 7, 6, "soflife", 4.8)
print(tuple1)
print(type(tuple1))
print(tuple1[3])

# dot notation and bracket notation in tuple
# use the index function to find the particular position of an element
print(tuple1.index(3))
print(tuple1.index(5))
print(tuple1.count(4))  # number of times an element appears

# tupleToList
tupleToList = list(tuple1)
print(tupleToList)  # to list all the element use list()
print(type(tupleToList))  # a class list

# change a data type into tuple
# convert a python list into a tuple
num = [1, 2, 4]  # Python list
listTuple = tuple(num)
print(listTuple)
print(type(listTuple))

print()
# ? how to use .partition
txt = 'I could eat bananas all day'
x = txt.partition('apples')
print(x)
x1 = txt.upper()
print(x1)
x2 = txt.count('o')
print(x2)
x3 = txt.index('e')
print(x3)

print()
# *Condtional Statement in Python

# conditonal statement is use to handle condtions in your program
# especially in decision making
# conditional statement guides the program while making decisions
# based on the condtions encountered by the program.

# ? we use the comparison operator (Type of Operators) in python to compare values of
# ? two conditons is met or not / if it is true or false.

# ? if statement executes a block of code only if our statement is true

cash = 4
if cash < 10:
    print("Buy veggies")

   # else statement is used when a conditon is false
   # ? Example

cash1 = 7
if cash1 > 10:
    print("Bring my money back")
else:
    print("The money is not enough")

# ? Example using condtional statement with comparison operators

cash3 = 10
if cash3 == 5:
    print("The currency value is low")
else:
    print("Improve our currency")
    print("Livibg is getting hard")

# ? Example
cash5 = 100
if cash5 == 100:
    print("The currency value is improving")
else:
    print("Devalue our currency")

# ? Example
cash2 = 6
if cash != 10:
    print("Things are expensive")
    print("Inflation")


# ? Example elif

cash5 = 80  # once the first line doesnt match, python checks the next line
if cash5 == 90:
    print("I have enough money")
elif cash5 == 80:
    print("I can afford it")
elif cash5 == 70:
    print("I can afford to pay for it")


# Combining condtions together
money = 20
if money == 100 or money == 80 or money == 60:
    print("I am poor")  # this prints when any of these conditions are met
else:
    print("I am rich")  # this prints once none of the first condition is met


# LOOPS IN PYTHON
