## Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

lis = ["Apple", "Mango", "Pineapple", "kiwi", "Circle"]
newlist = []

for i in lis:
    if "e" in i:
        newlist.append(i)

print(newlist)

## but in list comprehension

"""The Syntax
newlist = [expression for item in iterable if condition == True]"""

lis = ["Apple", "Mango", "Pineapple", "kiwi", "Circle"]
# first i the regular loop expression variable 2nd i refers to the stored items
# the condition is optional its for filtering i for i in listname 
newlis = [i for i in lis if "i" in i]

print(newlis)

# to create an iterable we use range(limit) function

newl = [i for i in range(10) if i == 5]

print(newl)
"""
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list
"""
newl1 = [i.upper() for i in lis]
newl2 = ["Hello" for i in lis]
print(newl1)
print(newl2)

## Using expression as condition both( if and else)
# Return "banana" instead of "Apple" :

newl3 = [i if i != "Apple" else "banana" for i in lis]
print(newl3)