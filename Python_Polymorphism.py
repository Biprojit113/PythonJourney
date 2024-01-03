"""
Python Polymorphism

many forms

In programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
"""


#Function Polymorphism
#An example of a Python function that can be used on different objects is the len() function.

l = ["Lol", "Ass"]
t = ("Lol", "Ass")
s = "Lol"
d = {
    "car": "fancy",
    "gear": "classy",
    "found": 1979
}

print(len(l))
print(len(t))
print(len(s))
print(len(d))

#Class Polymorphism
#Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

#For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

class Car:
    
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
     print("Drive")
class Boat:
   def __init__(self,brand,model):
      self.brand = brand
      self.model = model
   def move(self):
     print("Sail")
      
class Plane:
   def __init__(self,brand,model):
      self.brand = brand
      self.model = model

   def move(self):
    print("Fly")







car1 = Car("Honda", "Maruti")
car2= Boat("ibiza", "Touring 20")
car3 = Plane("Boeing","747")

car1.move()
car2.move()

#or


for x in (car1,car2,car3):
   x.move()


#Inheritance Class Polymorphism
#Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
class Vehicle:
   def __init__(self,brand,model):
      self.brand = brand
      self.model = model


class Car(Vehicle):
   def move(self):
      print("Drive")

class Boat(Vehicle):
   def move(self):
      print("Sail")

class Plane(Vehicle):
   def move(self):
      print("fly")


car1 = Car("Ford", "Mustang")
car2 = Boat("ibiza", "Tourin 20")
car3 = Plane("Boeing", "707")

for x in (car1,car2,car3):
   
   print(x.brand)
   print(x.model)
   x.move()

"""
In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

Because of polymorphism we can execute the same method for all classes.
"""