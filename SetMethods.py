#add()
#remove()
#clear()
#copy()
A = {1, 'There', 'You', 'Hi', 11, 'Are', 'Hello', 'How'}
x = A.copy()        #set.copy()
print(x)
#difference() method
#Meaning: The returned set contains items that exist only in the first set, and not in both sets.
#set.difference(set)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)  #it will store only the values that exit in x not in y
print(z) 

k = y.difference(x)
print(k)

#difference_update()method
"""
difference_update() method removes the items that exist in both sets.
difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
set.difference_update(set)
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)  #just updating the set 
print(x)

#intersection() method
"""
intersection() method returns a set that contains the similarity between two or more sets.
set.intersection(set1, set2 ... etc)
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)  # will store only the item which is present in both sets
print(z)

x = {'a','b','c'}
y = {'d', 'b', 'e'}
z = {'f','b', 'g'}

k = x.intersection(y,z)
print(k) # {'b'} cause b present in x,y,z sets


#intersection_update() method
"""
intersection_update() method removes the items that is not present in both sets
 the intersection() method returns a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.
 set.intersection_update(set1, set2 ... etc)
"""

x = {'a','b','c'}
y = {'d', 'b', 'e'}
z = {'f','b', 'g'}

x.intersection_update(y,z) #by comparing with y and z
print(x)

#isdisjoint() method

"""
isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
set.isdisjoint(set)
"""

x = {'a','b','c'}
y = {'d', 'h', 'e'}
z = {'f','b', 'g'}

k = x.isdisjoint(y)
print(k) #True as no items are matched

k = x.isdisjoint(z)
print(k)

#issubset()
"""
Return True if all items in set x are present in set y:
issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
set.issubset(set)
"""
x = {'a','b','c'}#subset
y = {'d', 'h', 'e','a','b','c'} #superset
z = {'f','b', 'g'} #only a set

k = x.issubset(y)  #returns true if all the items of x is present in y
print(k)

l = x.issubset(z)
print(l)

#issuperset() method
"""
Return True if all items set y are present in set x:
issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False
set.issuperset(set)
"""

x = {'a','b','c','d', 'h', 'e','b', 'g'} #Superset
y = {'d', 'h', 'e'}#subset
z = {'f','b', 'g'} # only a set

k = x.issuperset(y)
print(k)

l = x.issuperset(z)
print(l)

#symmetric_difference() method
"""
Return a set that contains all items from both sets, except items that are present in both sets:
symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
set.symmetric_difference(set)
"""
x = {'a','b','c'}
y = {'d', 'h', 'e'}
z = {'f','b', 'g'}

k = x.symmetric_difference(y) #stores all the items in x and y but except similar items
print(k)

l = x.symmetric_difference(z)
print(l) # won't print b cuz its i both set

#symmetric_difference_update()
"""
symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.
set.symmetric_difference_update(set)
"""
x = {'a','b','c'}
y = {'d', 'h', 'e'}
z = {'f','b', 'g'}

x.symmetric_difference_update(y)
print(x)

x = {'a','b','c'}
x.symmetric_difference_update(z) # only updating the x no need for new set
print(x)