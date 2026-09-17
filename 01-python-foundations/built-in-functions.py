# Now, we will explore python's variables and built-in functions.

# According to the official Python documentation (https://docs.python.org/3/library/functions.html), we have lots of built-in functions.
#Here're the most commonly used built-in functions in Python:

print ("Hello Andromeda") # This is a function that prints any string, number, or variable to the console. In this case, it prints the string "Hello Andromeda".

len ("Hello Andromeda") # This is a function that returns the length of any string, list, tuple, or dictionary. In this case, it returns the length of the string "Hello Andromeda".
print (len ("Hello Andromeda")) # If we want to see the length of the string "Hello Andromeda", we can use the print function to print the result of the len function.

type ("Hello Andromeda") # This is a function that returns the type of any variable, string, list, tuple, or dictionary. In this case, it returns the type of the string "Hello Andromeda".
print (type ("Hello Andromeda")) # If we want to see the type of the string "Hello Andromeda", we can use the print function to print the result of the type function.

str (4) # This is a function that converts any variable, number, or string to a string. In this case, it converts the number 4 to a string.
print (str (4)) # If we want to see the string representation of the number 4, we can use the print function to print the result of the str function.
print (type(str (4))) # If we want to see the string representation of the number 4, we can use the print function to print the result of the str function, as well as the type function to see that it is indeed a string.

int (4.5) # This is a function that converts any variable, number, or string to an integer. In this case, it converts the float 4.5 to an integer rounding down to the nearest whole number, which is 4.
print (int (4.5)) # If we want to see the integer representation of the float 4.5, we can use the print function to print the result of the int function.
print (type(int (4.5))) # If we want to see the integer representation of the float 4.5, we can use the print function to print the result of the int function, as well as the type function to see that it is indeed an integer.

float (4) # This is a function that converts any variable, number, or string to a float. In this case, it converts the integer 4 to a float, which is 4.0.
print (float (4)) # If we want to see the float representation of the integer 4, we can use the print function to print the result of the float function.
print (type(float (4))) # If we want to see the float representation of the integer 4, we can use the print function to print the result of the float function, as well as the type function to see that it is indeed a float.

input("What galaxy are you from? = ") # This is a function that takes input from the user. In this case, it asks the user "What galaxy are you from?" and waits for the user to type their answer and press enter.
# exit() #This is a function that exits the program, but it is explained through a comment because we do not want to exit the program, as we will develop more code afterwards. However, it is good practice to use the exit() function to explicitly exit the program when we are done with it.
# Although we can use the exit() function to exit the program, it is also not necessary to use it in this case because the program will automatically exit after the user has typed their answer and pressed enter. However, it is good practice to use the exit() function to explicitly exit the program when we are done with it.
# We have several exit functions in Python, such as sys.exit(), os._exit(), and quit(). However, we will not be using them in this course because they are not necessary for our purposes. We will only be using the exit() function to exit the program when we are done with it.
# We also have exit (0) and exit (1) functions in Python, which are used to exit the program with a status code. The exit (0) function is used to indicate that the program has exited successfully, while the exit (1) function is used to indicate that the program has exited with an error. However, we will not be using them in this course because they are not necessary for our purposes. We will only be using the exit() function to exit the program when we are done with it.

help() # This is a function that provides help and documentation for any function, module, or class in Python. In this case, it provides help and documentation for the built-in functions in Python.
help("keywords") # This functions helps us to see the list of keywords in Python. Keywords are reserved words that have special meaning in Python and cannot be used as variable names or function names.
help(str) # This function provides help and documentation for the str class in Python.
dir() # This is a function that returns a list of the attributes and methods of any object, module, or class in Python. In this case, it returns a list of the attributes and methods of the built-in functions in Python.
dir(str) # This function returns a list of the attributes and methods of the str class in Python.

min (4, 5, 6, 7, 8) # This is a function that returns the smallest number from a list of numbers. In this case, it returns the smallest number from the list [4, 5, 6, 7, 8], which is 4.
print (min (4, 5, 6, 7, 8)) # If we want to see the smallest number from the list [4, 5, 6, 7, 8], we can use the print function to print the result of the min function.
max (4, 5, 6, 7, 8) # This is a function that returns the largest number from a list of numbers. In this case, it returns the largest number from the list [4, 5, 6, 7, 8], which is 8.
print (max (4, 5, 6, 7, 8)) # If we want to see the largest number from the list [4, 5, 6, 7, 8], we can use the print function to print the result of the max function.
sum (4, 5, 6, 7, 8) # This is a function that returns the sum of a list of numbers. In this case, it returns the sum of the list [4, 5, 6, 7, 8], which is 30.
print (sum (4, 5, 6, 7, 8)) # If we want to see the sum of the list [4, 5, 6, 7, 8], we can use the print function to print the result of the sum function.

# We can also use the min and max functions with a list of numbers, instead of passing the numbers as separate arguments. For example, we can use the min function with a list of numbers like this:

min ([4, 5, 6, 7, 8]) # This is a function that returns the smallest number from a list of numbers. In this case, it returns the smallest number from the list [4, 5, 6, 7, 8], which is 4.
print (min ([4, 5, 6, 7, 8])) # If we want to see the smallest number from the list [4, 5, 6, 7, 8], we can use the print function to print the result of the min function.
max ([4, 5, 6, 7, 8]) # This is a function that returns the largest number from a list of numbers. In this case, it returns the largest number from the list [4, 5, 6, 7, 8], which is 8.
print (max ([4, 5, 6, 7, 8])) # If we want to see the largest number from the list [4, 5, 6, 7, 8], we can use the print function to print the result of the max function.
sum ([4, 5, 6, 7, 8]) # This is a function that returns the sum of a list of numbers. In this case, it returns the sum of the list [4, 5, 6, 7, 8], which is 30.
print (sum ([4, 5, 6, 7, 8])) # If we want to see the sum of the list [4, 5, 6, 7, 8], we can use the print function to print the result of the sum function.
# exit (0) #This is a function that exits the program with a status code of 0, which indicates that the program has exited successfully. We can use the exit() function to explicitly exit the program when we are done with it.

# Here are more built-in functions in Python that we can use, actually, I will list all of them:

abs() # Returns the absolute value of a number.
all() # Function that returns true if every element in an iterable object is truthy.
any() # Function that returns true if at least one element in an iterable object is truthy.
asci() # Replaces any non-ASCII characters.
bin() # Converts an integer into its binary representation (base-2) as a string precedeb by "0b".
bool() # Converts any value into a boolean value.
breakpoint() # It drops you directly into an interactive debugging session right in your terminal.
bytearray() # It returns a mutable sequence of bytes, each item inside a bytearray must be an integer between 0 and 255 (representing an 8-bit byte)
bytes() # It's the same as a bytearray, but it's not mutable.
callable() # It tells you wether you can put a parenthesis at the end of that string or not.
chr() # It takes an integer number and converts it into its matching text character based on the computer's universal master dictionary (Unicode/ASCII)
classmethod() # It's a shortcut for creating classes.
compile() # Takes a string containing Python code and converts it into something Python can actually understand and rut later (code objetc).
complex() # It creates a complex number.
delattr() # It permanently removes an attribute from an object on the fly.
dict() # Function to create a dictionary in python.
dir() # It returns a sorted list of all the valid attributes and methods belonging to an object. 
divmod() # Takes two numbers, performs a division, and returns a tuple containing two results at the same time (floor division and the remainder).
enumerate() # It keeps track of both the item and its index position at the same time.
eval() # It takes a string of text containing a Python expression and it dynamically runs it as real Python code.
exec() # It behaves alike eval(), although it can run complex. multi-line Python code, which differs from eval().
filter() # It filters out data from a list (iterable) that returns False from the function parsed inside filter().
format() # Converts a value into a formatted string based on a specific set of styling rules.
frozenset() # Creates an inmutable version of a standard set.
getattr() # Function to acces the value of an object's attribute by introducing its name as a string.
globals() # Returns a dictionary containing all global variables, functions and classes inside the current module.
hasattr() # Function used to check if an object has an attribute or method.
hash() # It takes and object as input and transformes it into hash (fixed-size integer representing its contents)
help() # Instant official instructions and documentation.
hex() # It converts an integer into its lowercase hexadecimal (base-16) string representation, prefixed with 0x.
id() # Returns the unique ID integer of an object (it's like the location of that data in the memory of python).
input() # Function that enables to ask and collect inputs from the user running the program.
int() # Converts the content of the object (has to be a float or a numeric string) parsed into an integer.
isinstance() # Enables you to check if an object belongs to a specific class or data type.
issubclass() # It is used to check if the class parsed is a subclass (child) of another class.
iter() # Helps you load an iterator and have the data available without fully loading it.
len() # Enables you to see the lenght of the object parsed.
list() # Enables you to build a list of objects
locals() # Returns a dictionary containing all the local variables and functions defines in the current scope/python file.
map() # Facilitates the work of locating and manipulating content inside a list without using for nor loops.
max() # Returns the largest item in an iterable or from 2 or more arguments.
memoryview() # Allows you to access and slice data through the internal binary buffer of an object and without making a copy of it.
min() # Returns the smallest item in an iterable or the smallest of two or more arguments.
next() # Used to extract the very next item from an iterator.
object() # Returns a blank, featureless objet.
oct() # Converts an integer into its octal (base-8) string representation.
open() # It opens a file and returnns the corresponding file object.
ord() # It converts a single character into its corresponding Unicode code point or ASCII integer value.
pow() # Function used to perform exponentiation and can accept a third argument which corresponds for an optional modulus.
print() # It prints the content inside the parenthesis.
property() # Used when we want to validate and restrict the possibilities when 
range() 
repr() 
reversed() 
round() 
set() 
setattr() 
slice() 
sorted() 
staticmethod() 
str() 
sum() 
super() 
tuple() 
type() 
vars() 
zip() 
__import__() 