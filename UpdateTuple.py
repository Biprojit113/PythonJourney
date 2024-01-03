#You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# Tuple is unchangeable directly

tup = ('People', "Won't", 'Remember', 'You')
convertingToList = list(tup) #converting to list
#making changes
convertingToList[0] = "Someday"  
convertingToList.insert(1,"People")
convertingToList.append("Even")
convertingToList.remove("Even")
#converting to tuple
convertingToTuple = tuple(convertingToList)  
print(convertingToTuple)


convertingToTuple = tuple(convertingToList)
del convertingToTuple #delete del is a keyword which deletes the entire list or tuple similar like things

tu = ('Someday', 'Even', 'People')
tu2 = ("Remember",) #Only ("Remember") is a string not a tuple 

tu += tu2

print(tu)
del tu
#print(tu)  #NameError: name 'tu' is not defined.  that means tuple is deleted