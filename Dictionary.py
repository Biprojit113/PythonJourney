"""
Dictionaries are used to store data values in key:value pairs.
ordered*, changeable and do not allow duplicates.

{} AND have keys and values:       
can be referred to by using the key name.


"""


dicto = {
    "car": "Lamborgini",
   #  Key :   Value    
    "color" : "White",
    "speed"  :  "300Kmh",
    "price"  : "3.5 million euro",
    "year"   : 2022, #this will be overwritted by year : 2023  that proves in dictionary duplicate values are not alowed
    "year"   : 2023,
    "Suprecar" : True,
    "Manufacturer" : [ "A", "B", "C"] #list
    
    }

print(dicto)

# input what is the speed of lamborgini then output is->
print(dicto["car"])  # values are reffered through there keys
print(dicto["speed"])
print(dicto["year"])
print(len(dicto)) #year 2022 is overwritted
print(range(len(dicto)))
print(dicto["Suprecar"])
print(type(dicto)) # <class 'dict'> dictionary datatype of python
print(dicto["Manufacturer"])

# dict() method to make a dictionary:

dictio = dict(name = "Koly", age = 24, sex = "Female")

print(dictio)


"""
Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


"""


