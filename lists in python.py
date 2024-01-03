mylist = [ "hello", "How are you holding up", "I gotta go now! Byee!!"]

print(mylist)
print(len(mylist))
print(mylist[0],mylist[1]) #INPUTED IN ORDER LIST
#print(mylist.insert(1,'Cat'))
mylist.append("Hi")  # to insert a string at the end ina list we use append method
print(mylist)
mylist.insert(2,"Hello") # to add a value in specific area in a list insert function(insertion area,inserted value) is used
print(mylist)

koro = [ "Hello", 1,2,2,2,2, True,False, "Wassup Guys" ]

print(koro)

print(type(mylist))#to know the type of mylist

print(type(koro))


#creating a new list with list() constructor

itlist = list(("apple","juice", "is the best"))
print(itlist)

