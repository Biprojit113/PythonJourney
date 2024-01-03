"""
update() method 
update() method will update the dictionary with the items from the given argument.
The argument must be a dictionary, or an iterable object with key:value pairs.
{key:value}

"""

inside = {
   "Sports" : "Cricket",
   "Country" : "Bangladesh",
   "Born"   : 1975,
   "Tropies" : None
}

k = inside.update({"Tropies" : 1}) #dict.update({Key:value})
print(inside)

