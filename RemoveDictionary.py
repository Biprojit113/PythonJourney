"""
pop() method removes the item with the specified key name:

popitem() will delete the last inserted value (Not important)

del keyword removes the item with the specified key name:
del also can delete the dictionary completely
clear() method empties the dictionary

"""

inside = {
   "Sports" : "Cricket",
   "Country" : "Bangladesh",
   "Born"   : 1975,
   "Tropies" : None
}

inside.pop("Tropies")  #using pop() 
print(inside)

inside.popitem()  #using popitem()
print(inside)

del inside["Country"]  
print(inside)

inside.clear()
print(inside)

del inside
print(inside)




