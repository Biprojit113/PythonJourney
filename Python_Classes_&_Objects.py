"""
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

"""


class newclass :   #creating a class which is the blueprint of objects which we are gonna create
    x = 24   # the components of newclass class 

obj1 = newclass()           # object of that class
print(obj1.x)                   # printing the value by declare the class as object and through that obect we are able to print the value

# creating a class with __int__ function

"""
The __init__() Function
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

NOTE: The __init__() function is called automatically every time the class is being used to create a new object.

Create a class named Person, use the __init__() function to assign values for name and age:

"""
class outclass:
 def printself(self):
   print("This is me "+ self.name)

ob1 = outclass()
ob1.name = "John"
ob1.age = 21  
ob1.printself() 

ob2 = outclass()
ob2.name = "Carry"
ob2.age = 26
ob2.printself()

#Now to solve the complexity of different objects properties we use __init__ ()(underscore underscore initunderscore underscore )

          

class viewclass:
    def __init__(self,name,age):              #everytime a new object is needed to be created in __init__ function will call the class itself  
        self.name = name 
        self.age = age
    
    def overview(self):
     print("This is my name "+self.name)


p1 = viewclass("Rohan", 24)
p2 = viewclass("Lucas", 27)
p1.overview()
p2.overview()

print(p1.age)
print(p2.age)

#Simplified easily

"""
Self : This instance of the class


The __str__() Function

The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:
"""
#The string representation of an object WITHOUT the __str__() function:

class new1 :
   def __init__(self,name,looks):
      self.name = name
      self.looks = looks
    
f1  =  new1("Hello", 100)
print(f1)  #<__main__.new1 object at 0x0000025E293AFED0> we don't specify here what should return string


class new2:
   def __init__(self,name,looks):
      self.name = name
      self.looks = looks

   def __str__(self):              #built in function/constractor __str__() refers to the string of that object will be returned in object
      return(f"Name:{self.name}  Look:{self.looks}%")
   #f"" format spectors is to use it to print multiple datatype at one print with different spectators


f2 = new2("Luke", 100)  #Stored Name:Luke  Look:100
print(f2) 


"""
Objects can also contain methods. Methods in objects are functions that belong to the object.
Insert a function that prints a greeting, and execute it on the p1 object:
"""

class class2:
   def __init__(self, name, age):
      self.name = name
      self.age = age
    
   def myfu(self):           #object method
      print("Hello i am  "+self.name)

p1 = class2("John", 45)
p1.myfu()  #belongs to the object p1


"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""

#Use the words mysillyobject and abc instead of self:

class class1:
   def __init__(mysillyobject,name, age):
      mysillyobject.name = name
      mysillyobject.age = age
   def __str__(abc):
      return(f"NAME: {abc.name}   AGE: {abc.age}")


p1 = class1("Terry", 46)
#Set the age of p1 to 40
p1.age = 40
p1.name = "Cena"
print(p1)
#Delete the age property from the p1 object:
del p1.age
#Delete the p1 object:
del p1
print(p1)

#class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class empty:
   pass




