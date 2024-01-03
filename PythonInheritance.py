"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.



"""

#Create a class named Person, with firstname and lastname properties, and a printname method:
#Its a parrent class
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print("The persons name is "+self.fname+" " +self.lname)

p1 = person("Jhonny", "Deep")
p1.printname()

#making a child class of parrent class
"""
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

"""
#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(person):
    pass                   #if we don't need to add any extra properties to the child class beside parent class properties use pass

#Use the Student class to create an object, and then execute the printname method:
x = Student("Jhonny", "Sins")
x.printname() #The persons name is Jhonny Sins

#We want to add the __init__() function to the child class (instead of the pass keyword).
#Add the __init__() function to the Student class:

class student(person):
    def __init__(self,fname,lname):
        
     person.__init__(self,fname,lname)
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#NOTE: The child's __init__() function overrides the inheritance of the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

x= student("Joker", "Boy")
x.printname()


#super() Function
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class stud(person):
    def __init__(self,fname,lname, year): #the parameter year will come through stud class
        super().__init__(fname,lname)
        self.graduationyear = year
#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
#Add a year parameter, and pass the correct year when creating objects:
#Adding an method named welcome to the stud class
    def welcome(self):
        print(f"Welcome {self.fname} {self.lname} to the class of {self.graduationyear} ")

k = stud("Rockey", "Dusan", 2019)
k.printname()
print(k.graduationyear)
k.welcome()

#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
