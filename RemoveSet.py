"""
remove()method
Note: If the item to remove does not exist, remove() will raise an error.

discard() method
Note: If the item to remove does not exist, discard() will NOT raise an error.

pop()
it will remove a random item cuz the set is unordered so its pretty useless here but better to know the reason

"""

A = {'Hi', 1, 'LOVE', 'There', 'Are', 11, 'You', 'How', 'LOL', 'Hello'}

A.remove("LOL")
print(A)
"""
A.remove("LO")
print(A)

    A.remove("LO")
KeyError: 'LO'
"""

A.discard("LOVE")
print(A)

A.discard("LOV")
print(A)

#The clear() method empties the set:
A.clear()
print(A)  #set() it means empty set

#The del keyword will delete the set completely:
#del A 
#print(A) #NameError: name 'A' is not defined