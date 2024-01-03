"""
clear()
copy()
get()
items()
keys()
pop()
popitem()
update()
values()

"""
"""
fromkeys()method
fromkeys() method returns a dictionary with the specified keys and the specified value.
dict.fromkeys(keys, value)

"""
#Create a dictionary with 3 keys, all with the value 0 using fromkeys() method


x =  {"key1","key2", "key3"}
y = 0

k = dict.fromkeys(x,y)
print(k)

x =  {"key1","key2", "key3"}

k = dict.fromkeys(x) #{'key1': None, 'key3': None, 'key2': None}
print(k)

x = {"Country", "Sports", "Born"}
y = {"Bangladesh", "Cricket", 1979}

k  = dict.fromkeys(x,y)
print(k)

"""
setdefault() method
setdefault() method returns the value of the item with the specified key.
dictionary.setdefault(keyname, value)
value------>>>>>>  Optional.
If the key exist, this parameter has no effect.
If the key does not exist, this value becomes the key's value
Default value None


"""
inside = {
   "Sports" : "Cricket",
   "Country" : "Bangladesh",
   "Born"   : 1975,
   "Tropies" : None
}

k = inside.setdefault("Sports")
print(k)

l = inside.setdefault("color", "Red and Green") #'color': 'Red and Green'} it will first add the key with value in inside dict and then print the value Red and Green         
print(inside)
print(l)