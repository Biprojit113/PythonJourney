"""
   Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
   Tuples are written with round brackets.
 we cannot change, add or remove items after the tuple has been created.

"""

lol = ("banana", "lori", "lol","lol")
print(type(lol))

#One item tuple, remember the comma:

lol = ("Koli",)
print(type(lol))#tuple

lol=("lol")
print(type(lol))#not tuple

tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))


##--> tuple() constructor to make a tuple.
atuple = tuple(("Hello", 1, 2, 3))

print(type(atuple))


############################### Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

