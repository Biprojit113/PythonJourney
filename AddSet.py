"""
Add an item to a set, using the add() method:

To add items from another set into the current set, use the update() method.
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

"""

B = {'Are', 'You', 'There', 'How', 'Hello'}
B.add("Hi")  #using add method to add one value
print(B)

# using update()method to add another set values or other datatypes of python

A = {"LOVE", "LOL", 1, 11}

B.update(A)
print(B)


A  = ("Did", "I") #Tuple

B.update(A)
print(B)

