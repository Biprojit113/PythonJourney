"""
Python Modules
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.

Create a Module
To create a module just save the code you want in a file with the file extension .py:

"""
"""
Use a Module
Now we can use the module we just created, by using the import statement:

"""
#Import the module named mymodule, and call the greeting function:
import my_module
my_module.greeting("Beast")

#another way
from my_module import greeting # or * which means all functions from my_module
greeting("Helen")

"""
Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

"""

import my_module

l = my_module.lust["duration"]
print(l)

#another way 


from my_module import lust  # or *

print(lust["type2"])

"""
Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module
You can create an alias when you import a module, by using the as keyword:
"""

import my_module as mx    #module alise as mx

mx.greeting("Jake")

#Another way 

from my_module import greeting as greet   #module file as greet

greet("Tori")


"""
Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.
"""
#Import and use the platform module:

import platform
x = platform.system()
print(x)

"""
Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
"""

import platform 

x= dir(platform)
print(x)

import my_module

x = dir(my_module)

print(x)

