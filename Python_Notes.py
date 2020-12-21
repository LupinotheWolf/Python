"""
Python Notes
"""
"""
Intro Notes
"""
#Variable Types:
28 #Integer
1.5 #Float
'Hello', "Hello", """Hello""" #String
True, False #Booleans
None #NoneType

input("Text") #Asks user to input data into variable
variable = input("Please Enter Text!")

#Formatted Strings
print(f"Hello, {name}") #Will replace variable with the value
#If you have multiple variables inside and only change one, you need to add second set of {} to include

#This will replace %d with the value inside empCount
print("Total Employee %d" %Employee.empCount)
"New Line: \n" #Line break, will print new line
{var:f} #Will format variable into a float
{var:.2f} #Will format it toa float but only keep 2 decimal places
format(var, ".2f") #Will format into a string with a float with 2 decimals

variable = int() #Will make the argument an int
from functions import square #Will lookup function square() from the file called functions
#You can import from another file in the same folder

import functions #Will import entirety of functions from the file
#will need to be called by functions.square()
#If you import a file from the same folder, just name the file without the .py extention

import datetime #Imports datetime module, including tools for seeing dates and times
#Create a function called now, bringing the current date and time to the code
now = datetime.datetime.now()
now.year, now.month, now.day, etc #Will bring current year, month, etc..

"""
Testing Values
"""
len() #Will give length of the value inside, like a set or a list or a string etc
range(6) #Gives a range of numbers from 0 to 6

test = input("input a number: ")
try: #Will try to do something, to give an exception if there's an error
    test = int(test)
    print("This is valid") #Be sure to pick up what the error is called
except ValueError: #If a value error comes up, it will do the following functions
    print("Not a valid number")
#ValueErrors is if a string was given and looking for an int for example
#Useful if you want to ask for a specific type of data from the user

#Conditionals:
x > 3, x < 3
x == 4 #Tests if it's equal
x >= 3, x <= 4 #Less/greater than or equal to
x ** 2 #x to the power of two
x % 2 #Only gives you the remainder of the division
#2 % 2 is 0 because it divides evenly and doesn't give a remainder
#This is useful for checking if a number is even
x += 1 #Will add to the original 1, same as x = x + 1
str:string #Will create a string using variable
string.lower() #Will make string lowercase
string.upper() #Will make string in block capitals
string.title() #Will Capitalise the string like a title
string.format(new_var = 'X') #Will change variable inside string to what you set
assert is_instance(var, list) #Will raise an error if var is not the type in the second argument
#In this case, it will raise error if the var is not a list

#Logical Conditionals
if a > b: #Will test a condition, in this case if a is greater than b
    print("A > B")
if a > b or a > c: #Will check if one of the statements is true
    print("A is bigger than B or C")
if a > b and a > c:
    print("A is bigger than both B and C") #Will check to see if both statements are true

#If statements cannot be empty but if you have an if statement and want to avoid error:
if b > a:
    pass
#This will avoid error and keep the if statement empty

"""
Sequencing
"""
variable[0] #The number inside is the index of the variable

#Duples/Triples
variable = (10.0, 20.0) #Will keep two floats as info in the variable
#You will need to keep both arguments from now on in that variable

"""
Lists
"""
#Lists will always be ordered, whereas sets are unordered
names = ["Harry", "Ron", "Hermione"]
#Will save as a list and hole more than one string inside
names[0] #Gives you the value at the index 0 which is "Harry"
names.append("Draco") #Will add string 'Draco' to end of list
names.sort() #Will sort values automatically
sum(list) #Will do the sum of numbers in a list
len(list) #Will give you number of items in list as an int

"""
Sets
"""
#Sets are unordered lists of values
#!Any duplicate values won't be added!!
set = set() #Creates an empty set in variable set
set.add(1) #Adds a single int 1 to set
set.remove(1) #Removes the int 1 from the set

"""
Loops
"""
#For Loops
for i in [0, 1, 2]: #Will create a var called i for the function
    print(i) #will iterate i in every int inside an do the code
    #i is now the last item in the list so can be called if wanted
    #Use the else statement to do code after the loop is finished
else:
    print("Finished Loop!")

#Ranges
range(0, 10) #Create a range of ints from first number to second number

#While Loops
#Will continue to loop as long as the conditions are met
while x > 10:
    x += 1
    if > 100:
        break #Will break the loop if condition is met
while x < y:
    if x % 2 == 0:
        print("Even")
    else:
        continue #Will continue the loop if condition isn't met

"""
Classes
"""
"""
__init__ can be defined with many arguments as an object and self will be the object itself to consider in the arguments. If you initialise a Class, it will force you to input the arguments when you create an object inside that class. To avoid making it mandatory, you can skip initialising it and just make a class with attributes inside of it
Always initialise using self as the first argument because that makes it a real object
__str__  Including str in the class as a function will create a string representation of it, letting you print out the object name itself instead of its memory address
"""

class Car(object):
    def __init__(self, model, colour, company, speed_limit):
        self.colour = colour
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def __str__(self):
        return f"This is a {self.colour} car called the {self.company} {self.model}"

#Once you set a Class, you can add objects to that class with variables
Audi = Car("A6", "Red", "Audi", 80)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(2, 8)

#You can use an existing Class as an argument to make a new one
#This will override an attribute with the old class
class New_Class(Old_Class):
    new_param = 'new value'

"""
Dictionaries
"""
#Will create a pairing of keys and values
#Keys are the lookup word
#Values are the values inside the key
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
#"Harry" is the key and the value is "Gryffindor"
print(houses["Harry"]) #Will lookup the value inside the key of "Harry" and print that
houses.keys() #Will print only the keys
list(houses.keys()) #Will create a list using the keys inside
houses["Hermione"] = "Gryffindor" #Will lookup key "Hermione" and assign value of "Gryffindor"
#If the key/value doesn't exist, it will create a new entry

houses["Harry"] = "Slytherin" #Will update entry with the new value

"""
Functions
"""
def square(x): #Defines the function called square(x)
    return x * x
#x is the argument and will bring the values into the function
#Once it does the calculation, it will return the value to where the function was called

#Decorators
#Decorators wrap a function inside another function
#This lets you modify functions after you set them
def announce(f):
    def wrapper():
        print("About to run function...")
        f()
        print("Ran Function!")
#You can recall a decorator using @
@announce #Using this before a function will run the function within it
#In this case it will announce before and after the function that it will run
