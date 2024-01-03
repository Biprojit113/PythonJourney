"""
A variable is only available from inside the region it is created. This is called scope.

Local Scope

A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

"""


def fu():
    x = 45
    print("the local scope value is:", x)

fu()

#The local variable can be accessed from a function within the function:

def fu():
    x = 45
    def inner():
      print("the local scope value is:", x)
    inner()

fu()

"""
Global Scope
Global variables are available from within any scope, global and local.

"""
#A variable created outside of a function is global and can be used by anyone:

l = 89

def call():
   print("Global Value Inside The Function:",l)

call()
print("Global Varriable outside of the function :", l)


"""

Naming Variables
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

"""

#The function will print the local x, and then the code will print the global x:

i = 89

def chng():
   i = 90
   print("Global Value Inside The Function:",i)

chng()
print("Global Varriable outside of the function :", i)


#Global Keyword
#If you use the global keyword, the variable belongs to the global scope:

x= 11
def glo():
   global x
   x = 78
   print("Global keyword:", x)

glo()

print("After using global keyword the value of x is:", x) #global keyword permanently changes the memory value from 11 to 78

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x= 11
def glo():
   global x
   print("Global keyword:", x)
   x = 78

glo()

print("After using global keyword the value of x is:", x)


