"""
Set
Sets are used to store multiple items in a single variable.
unordered, unchangeable*, and unindexed.
 items are unchangeable, but you can remove items and add new items. do not allow duplicate values.
 Sets are written with curly brackets. 
 Note: Sets are unordered, so you cannot be sure in which order the items will appear.
 Once a set is created, you cannot change its items
 Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

"""

Set = {2,3,"Hello", "There",2,3,True, 3.5555}

print(type(Set))
print(Set) # the result will be unordered

Se = {1,2,3,"Hello", "There",2,3, True}

print(type(Se))
print(Se) # No duplicate numbers are allowed, Here True won't be in result set cuz python set considered True and 1 as duplicates.
#{1, 2, 3, 'There', 'Hello'}
print(len(Set)) # to find out the numbers of values in set


#set() constructor to create a Set

S = set(("Hello", "There", "How", "Are", "You"))
print(S)
print(len(S))
print(type(S))










###########Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
