# What is a modules?
# 
# -> A module is a file containing code written by somebody else (usually) which can be imported and used in our programs

# What is pip?
#
# Pip is a package manager for python. We can use pip to install a module on our system.
# For example: pip install flask (It will install flask in our system)

# There are two types of modules in python:
#
# 1. Built-in modules – Pre-installed in Python e.g. os, abc, etc.
# 2. External modules – Need to install using pip e.g. TensorFlow, flask, etc.


""" 
-------------------------------------------------
Variables - What is it?
-------------------------------------------------
# 0. A variable is a name given to a memory location in a program.

# 1. In python a variable is created the moment we first assign a value to it. 

    E.g. 

    x = 45
    y = 'John'
    print(x)
    print(y)

2. Variables do not need to be declared with any particular type, and can even change type after they have been set.

    E.g. 

    x = 4       # x is of type int
    x = "Sally" # x is now of type str
    print(x)


-------------------------------------------------
Data Types
-------------------------------------------------
# 0. Variables can store data of different types, and different types can do different things.

# 1. Python has the following data types built-in by default, in these categories:

    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview

# 2. We can get the data type of any object by using the type() function.

    E.g. 
    x = 5
    print(type(x)) 


-------------------------------------------------
Type Casting/Type Conversion/Casting
-------------------------------------------------
# 0. Converting one datatype into another is known as type casting or, type-conversion.

# 1. If we want to specify the data type of a variable, this can be done with casting.

# 2. Python uses classes to define data types, including primitive types. 

# 3. Casting in python is therefore done using constructor functions

    E.g. 
    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0


-------------------------------------------------
Python - Variable Names (Rules and Conventions)
-------------------------------------------------
# Rules for Python variables:

    (1) A variable name must start with a letter or the underscore character
    (2) A variable name cannot start with a number
    (3) A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    (4) Variable names are case-sensitive (age, Age and AGE are three different variables)

# Multi Words Variable Names: 
 
    1. Camel Case: Each word, except the first, starts with a capital letter.
        e.g. myVariableName = "John"
    
    2. Pascal Case: Each word starts with a capital letter.
        e.g. MyVariableName = "John"
    
    3. Snake Case: Each word is separated by an underscore character.
        e.g. my_variable_name = "John"
    
    4. Kebab Case (*Not in python): Like Snake Case, but using hyphens instead.
        e.g. first-name, main-section

    5. Screaming Case: This refers to names in uppercase.
        e.g. TAXRATE, TAX_RATE

    6. Hungarian Notation: Names start with a lowercase prefix to indicate intention. 
       Rest of the name is in Pascal Case. It comes in two variants: (a) Systems Hungarian, 
       where prefix indicates data type; (b) Apps Hungarian, where prefix indicates logical purpose. 
        e.g. strFirstName, arrUserNames for Systems; rwPosition, pchName for Apps.

"""

# Source-1: https://www.codewithharry.com/videos/python-tutorial-easy-for-beginners
# Source-2: https://www.w3schools.com/